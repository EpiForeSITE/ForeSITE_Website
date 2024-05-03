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
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

{% include section.html background="images/background.jpg" dark=true %}

## {% include icon.html icon="fa-solid fa-users" %}University of Utah Team


## {% include icon.html icon="fa-solid fa-users" %}Washington State University Team


## {% include icon.html icon="fa-solid fa-users" %}Project Mangement Team


# {% include icon.html icon="fa-solid fa-users" %}Public Health Partners

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
