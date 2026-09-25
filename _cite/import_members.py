"""
One-time import: fill in missing _members/*.md link fields (and empty bios)
from InsightNet's config/organizations/foresite.toml.

This is NOT wired into CI. Run it once locally, review the diff, and commit
the result:

    python _cite/import_members.py [--toml ../insightnet-ai/config/organizations/foresite.toml]

It only ADDS values -- an existing links.* entry, or a non-empty bio, is
never overwritten. Researchers in the TOML with no matching _members/*.md
file are printed as a report at the end (e.g. Olivia Banks has no ForeSITE
Website page yet) so a decision can be made about adding one.
"""

import argparse
import re
import tomllib
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
MEMBERS_DIR = REPO_ROOT / "_members"
DEFAULT_TOML = REPO_ROOT.parent / "insightnet-ai" / "config" / "organizations" / "foresite.toml"

ORCID_RE = re.compile(r"(\d{4}-\d{4}-\d{4}-\d{3}[\dX])")
MEMBER_PAGE_RE = re.compile(r"ForeSITE_Website/members/([^/]+)\.html", re.IGNORECASE)

# manual overrides for researchers whose TOML full_name doesn't exactly
# match the member file's `name:` front matter (a pre-existing typo in the
# member file, left untouched here)
NAME_OVERRIDES = {
    "yue-zhang": "Yue_Xhang.md",
}


def normalize(name):
    # strip parentheticals ("Nathorn (Nui) Chaiyakunapruk") and collapse space
    clean = re.sub(r"\([^)]*\)", " ", name)
    return re.sub(r"\s+", " ", clean).strip().lower()


def load_members():
    """Return {filename: (front_matter_dict, body_text)} for every member page."""
    members = {}
    for path in MEMBERS_DIR.glob("*.md"):
        text = path.read_text()
        parts = text.split("---", 2)
        if len(parts) < 3:
            print(f"WARNING: {path.name} has no parseable front matter, skipping")
            continue
        front = yaml.safe_load(parts[1]) or {}
        body = parts[2]
        members[path.name] = (front, body, path)
    return members


def find_member_file(researcher, members):
    website = researcher.get("website") or ""
    m = MEMBER_PAGE_RE.search(website)
    if m:
        slug = m.group(1)
        for filename in members:
            if filename[:-3].lower() == slug.lower():
                return filename

    rid = researcher.get("id")
    if rid in NAME_OVERRIDES:
        override = NAME_OVERRIDES[rid]
        if override in members:
            return override

    target = normalize(researcher["full_name"])
    for filename, (front, _, _) in members.items():
        if front.get("name") and normalize(front["name"]) == target:
            return filename

    return None


def extract_link_fields(researcher):
    """Return {links key: value} to add, per the mapping in types.yaml."""
    fields = {}

    orcid_url = researcher.get("orcid")
    if orcid_url:
        m = ORCID_RE.search(orcid_url)
        if m:
            fields["orcid"] = m.group(1)

    scholar = researcher.get("google_scholar")
    if scholar:
        m = re.search(r"[?&]user=([^&]+)", scholar)
        if m:
            fields["google-scholar"] = m.group(1)

    linkedin = researcher.get("linkedin")
    if linkedin:
        m = re.search(r"linkedin\.com/in/([^/?#]+)", linkedin)
        if m:
            fields["linkedin"] = m.group(1).rstrip("/")

    github = researcher.get("github")
    if github:
        m = re.search(r"github\.com/([^/?#]+)", github)
        if m:
            fields["github"] = m.group(1)

    bluesky = researcher.get("bluesky")
    if bluesky:
        fields["bluesky"] = bluesky

    website = researcher.get("website")
    if website and not MEMBER_PAGE_RE.search(website):
        fields["home-page"] = website

    return fields


def update_member(front, body, researcher):
    """Mutate front (in place) and return possibly-updated body. Returns
    True if anything changed."""
    changed = False

    links = front.get("links")
    if not isinstance(links, dict):
        links = {}
    new_fields = extract_link_fields(researcher)
    for key, value in new_fields.items():
        if key not in links or not links[key]:
            links[key] = value
            changed = True
    if links:
        front["links"] = links

    bio = researcher.get("bio")
    if bio and len(body.strip()) < 20:
        body = "\n" + bio.strip() + "\n"
        changed = True

    return changed, body


class IndentDumper(yaml.Dumper):
    """Indent block-sequence items under their parent key (PyYAML's default
    dumper aligns list items with the key instead), matching the existing
    member file style."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def dump_front_matter(front):
    IndentDumper.ignore_aliases = lambda *args: True
    return yaml.dump(
        front, Dumper=IndentDumper, default_flow_style=False, sort_keys=False, allow_unicode=True
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--toml", default=str(DEFAULT_TOML))
    args = parser.parse_args()

    researchers = tomllib.loads(Path(args.toml).read_text())["organization"]["researchers"]
    members = load_members()

    unmatched = []
    updated_files = []

    for researcher in researchers:
        filename = find_member_file(researcher, members)
        if not filename:
            unmatched.append(researcher["full_name"])
            continue

        front, body, path = members[filename]
        changed, body = update_member(front, body, researcher)
        if changed:
            # `body` already starts with the newline that followed the
            # original closing "---", so don't add another one here
            new_text = "---\n" + dump_front_matter(front) + "---" + body
            path.write_text(new_text)
            updated_files.append(filename)

    print(f"Updated {len(updated_files)} member file(s):")
    for f in sorted(updated_files):
        print(f"  {f}")

    if unmatched:
        print(f"\n{len(unmatched)} researcher(s) with no matching _members/*.md file:")
        for name in unmatched:
            print(f"  {name}")


if __name__ == "__main__":
    main()
