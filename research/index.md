---
title: Publications
nav:
  order: 2
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}ForeSITE Related Publications

{% include section.html %}

## {% include icon.html icon="fa-solid fa-star" %}Featured

{%
  include list.html
  data="citations"
  component="citation"
  filters="group: featured"
  style="rich"
%}

## {% include icon.html icon="fa-solid fa-list" %}All Publications

Publications by ForeSITE members are collected weekly from ORCID, PubMed,
Europe PMC, arXiv and Crossref by [InsightNet
Explorer](https://epiforesite.github.io/insightnet-explorer/), the
publication-tracking dashboard shared across the ForeSITE Network. ForeSITE
member authors are shown in **bold**.

{% include search-box.html %}
{% include search-info.html %}

{%
  include list.html
  data="citations"
  component="citation"
%}
