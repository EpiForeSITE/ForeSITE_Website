---
title: Team
nav:
  order: 3
  tooltip: About our team
---

ForeSITE is comprised of teams from academic and public health partners 

# {% include icon.html icon="fa-solid fa-users" %}Academic Team

## {% include icon.html icon="fa-solid fa-users" %}Leadership Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}

## {% include icon.html icon="fa-solid fa-users" %}University of Utah Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: uu" %}


## {% include icon.html icon="fa-solid fa-users" %}Washington State University Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: wsu" %}

## {% include icon.html icon="fa-solid fa-users" %}STEDI Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: stedi" %}

## {% include icon.html icon="fa-solid fa-users" %}WILDE Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: wilde" %}

## {% include icon.html icon="fa-solid fa-users" %}Project Mangement Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pm" %}

## {% include icon.html icon="fa-solid fa-users" %}Computational Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: comp" %}

## {% include icon.html icon="fa-solid fa-users" %}Visual Analytics Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: vis" %}

# {% include icon.html icon="fa-solid fa-users" %}State Public Health Partners

{% include section.html %}

{% include section.html background="images/background.jpg" dark=true %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
