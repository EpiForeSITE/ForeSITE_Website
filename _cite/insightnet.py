"""
Build _data/citations.yaml from the InsightNet Explorer publications dataset.

InsightNet (https://github.com/EpiForeSITE/insightnet-explorer) collects
publications for every ForeSITE-network researcher weekly from ORCID, Europe
PMC, PubMed, arXiv and Crossref, and publishes the merged result as
data/works.json + data/works-details.json. This script downloads (or reads
locally) those two files plus config/organizations/foresite.toml, keeps only
the works tagged for ForeSITE, and reshapes them into the citation schema
that _includes/citation.html already understands.

The hand-curated "featured" list in _data/sources.yaml is preserved: every
featured id is looked up in the InsightNet data, and if it isn't there (for
example, a very old paper InsightNet hasn't (re)collected), the existing
record already in _data/citations.yaml is carried over unchanged so nothing
featured ever silently disappears.

Usage:
    python _cite/insightnet.py                       # fetch from GitHub
    python _cite/insightnet.py --local ../insightnet-ai/data   # use local copy
"""

import argparse
import json
import re
import sys
import tomllib
import urllib.request
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "_data" / "citations.yaml"
SOURCES_FILE = REPO_ROOT / "_data" / "sources.yaml"

RAW_BASE = "https://raw.githubusercontent.com/EpiForeSITE/insightnet-explorer/main"
WORKS_URL = f"{RAW_BASE}/data/works.json"
DETAILS_URL = f"{RAW_BASE}/data/works-details.json"
TOML_URL = f"{RAW_BASE}/config/organizations/foresite.toml"

ORGANIZATION_ID = "foresite"

# InsightNet work "type" -> the type keys defined in _data/types.yaml
TYPE_MAP = {
    "article": "paper",
    "preprint": "preprint",
}

ORCID_RE = re.compile(r"(\d{4}-\d{4}-\d{4}-\d{3}[\dX])")


def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.load(response)


def fetch_text(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def load_data(args):
    """Return (works, details, researchers) from --local dir or GitHub."""
    if args.local:
        local = Path(args.local)
        works = json.loads((local / "works.json").read_text())
        details = json.loads((local / "works-details.json").read_text())
        toml_path = local.parent / "config" / "organizations" / "foresite.toml"
        researchers = tomllib.loads(toml_path.read_text())
    else:
        works = fetch_json(WORKS_URL)
        details = fetch_json(DETAILS_URL)
        researchers = tomllib.loads(fetch_text(TOML_URL))

    researcher_list = researchers["organization"]["researchers"]
    return works["works"], details["details"], researcher_list


def build_researcher_index(researchers):
    """Map researcher id -> (full_name, last_name, first_initial, orcid)."""
    index = {}
    for r in researchers:
        full_name = r["full_name"]
        # strip parentheticals, e.g. "Nathorn (Nui) Chaiyakunapruk"
        clean = re.sub(r"\([^)]*\)", " ", full_name)
        tokens = clean.split()
        if not tokens:
            continue
        last_name = tokens[-1]
        first_initial = tokens[0][0].upper()
        orcid = None
        if r.get("orcid"):
            m = ORCID_RE.search(r["orcid"])
            if m:
                orcid = m.group(1)
        rid = r.get("id")
        if rid:
            index[rid] = {
                "full_name": full_name,
                "last_name": last_name,
                "first_initial": first_initial,
                "orcid": orcid,
            }
    return index


def bold_member_authors(author_names, work, details, researcher_index):
    """Return author name list with ForeSITE-member names wrapped in **bold**."""
    author_records = details.get("authors", []) if details else []
    if not author_records:
        return author_names

    # candidate ForeSITE researchers tied to this specific work
    candidates = [
        researcher_index[rid]
        for rid in work.get("researcher_ids", [])
        if rid in researcher_index
    ]
    if not candidates:
        return author_names

    orcid_lookup = {c["orcid"]: c for c in candidates if c["orcid"]}

    bolded = []
    for i, name in enumerate(author_names):
        record = author_records[i] if i < len(author_records) else {}
        is_member = False

        author_orcid = (record or {}).get("orcid") or ""
        if author_orcid and author_orcid in orcid_lookup:
            is_member = True
        else:
            tokens = [t.upper().rstrip(".") for t in re.split(r"[\s,]+", name) if t]
            for c in candidates:
                last_upper = c["last_name"].upper()
                if last_upper in tokens:
                    others = [t for t in tokens if t != last_upper]
                    if any(t[:1] == c["first_initial"] for t in others if t):
                        is_member = True
                        break

        bolded.append(f"**{name}**" if is_member else name)
    return bolded


def work_id(work):
    if work.get("doi"):
        return f"doi:{work['doi'].lower()}"
    if work.get("pmid"):
        return f"pmid:{work['pmid']}"
    if work.get("arxiv_id"):
        return f"arxiv:{work['arxiv_id']}"
    return f"insightnet:{work['id']}"


def build_citation(work, details, researcher_index):
    detail = details.get(work["id"], {})
    authors = [a.get("name", "") for a in detail.get("authors", [])]
    authors = bold_member_authors(authors, work, detail, researcher_index)

    citation = {
        "id": work_id(work),
        "title": work.get("title") or "",
        "authors": authors,
        "publisher": work.get("venue") or work.get("preprint_server") or "",
        "date": work.get("published_at") or "",
        "link": work.get("url") or "",
        "type": TYPE_MAP.get(work.get("type"), "paper"),
        "year": work.get("year"),
    }
    return citation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local",
        help="Path to a local insightnet-ai data/ directory to read instead of "
        "downloading from GitHub (e.g. ../insightnet-ai/data)",
    )
    args = parser.parse_args()

    works, details, researchers = load_data(args)
    researcher_index = build_researcher_index(researchers)

    foresite_works = [w for w in works if ORGANIZATION_ID in w.get("organization_ids", [])]
    print(f"Found {len(foresite_works)} ForeSITE works in InsightNet data", file=sys.stderr)

    citations = [build_citation(w, details, researcher_index) for w in foresite_works]
    citations_by_id = {c["id"]: c for c in citations}

    # apply featured metadata (group + image) from sources.yaml
    sources = yaml.safe_load(SOURCES_FILE.read_text()) or []

    # load the existing citations.yaml as a fallback for featured ids that
    # InsightNet hasn't (yet) collected, so featured papers never disappear
    existing_citations = {}
    if OUTPUT_FILE.exists():
        existing = yaml.safe_load(OUTPUT_FILE.read_text()) or []
        existing_citations = {c["id"]: c for c in existing}

    missing_featured = []
    for source in sources:
        sid = source["id"]
        # normalize doi ids to lowercase to match work_id()
        lookup_id = f"doi:{sid[4:].lower()}" if sid.startswith("doi:") else sid

        if lookup_id in citations_by_id:
            citations_by_id[lookup_id]["group"] = source.get("group", "featured")
            if source.get("image"):
                citations_by_id[lookup_id]["image"] = source["image"]
        elif sid in existing_citations:
            fallback = dict(existing_citations[sid])
            fallback["group"] = source.get("group", "featured")
            if source.get("image"):
                fallback["image"] = source["image"]
            citations_by_id[sid] = fallback
        else:
            missing_featured.append(sid)

    if missing_featured:
        print(
            f"WARNING: {len(missing_featured)} featured id(s) not found in "
            f"InsightNet data or existing citations.yaml: {missing_featured}",
            file=sys.stderr,
        )

    all_citations = sorted(
        citations_by_id.values(), key=lambda c: c.get("date") or "", reverse=True
    )

    yaml.Dumper.ignore_aliases = lambda *args: True
    with open(OUTPUT_FILE, "w") as f:
        f.write("# DO NOT EDIT, GENERATED AUTOMATICALLY\n\n")
        yaml.dump(all_citations, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Wrote {len(all_citations)} citations to {OUTPUT_FILE}", file=sys.stderr)


if __name__ == "__main__":
    main()
