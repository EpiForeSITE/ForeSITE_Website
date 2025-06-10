---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Academic Team

## {% include icon.html icon="fa-solid fa-users" %}Leadership Team

{% include section.html %}
{% include list.html data="members" component="portrait" filters="role: pi" %}

## {% include icon.html icon="fa-solid fa-users" %}Analytical Modeling Team
The analytical modeling team is comprised of members specializing in anomaly detection, parameter estimation, scenario modeling, and/or forecasting.

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: mod" %}

## {% include icon.html icon="fa-solid fa-users" %}Economic Impact Analysis Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: econ" %}

## {% include icon.html icon="fa-solid fa-users" %}Sociotechnical System Evaluation, Design & Implementation Team (STEDI)

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: stedi" %}

## {% include icon.html icon="fa-solid fa-users" %}Subject Matter Experts Responding to Disease Emergencies

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: sme" %}

## {% include icon.html icon="fa-solid fa-users" %}Project Management Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pm" %}

## {% include icon.html icon="fa-solid fa-users" %}Computational & Visual Analytics Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: comp" %}

# {% include icon.html icon="fa-solid fa-users" %}State Public Health Partners

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: state" %}

# {% include icon.html icon="fa-solid fa-users" %}Local Public Health Partners

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: local" %}

# {% include icon.html icon="fa-solid fa-users" %}Healthcare System Partners

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: hcs" %}


{% include section.html dark=true %}

{% include section.html %}

{% capture content %}

{% include figure.html image="images/Samore_CDC.png" %}
{% include figure.html image="images/Collingwood_CFA.png" %}
{% include figure.html image="images/CFA group.png" %}
{% include figure.html image="images/Richpresents.jpeg" %}


{% endcapture %}

{% include grid.html style="square" content=content %}
