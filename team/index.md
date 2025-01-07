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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Image Grid</title>
  <style>
    /* General page styling */
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Container for the grid */
    .image-grid {
      display: grid;
      grid-template-columns: 50% 50%;
      grid-gap: 10px;
      width: 100%;
      max-width: 100%;
    }

    /* Styling for images */
    .image-grid img {
      width: 100%;
      height: auto;
      object-fit: cover;
    }

    /* Optional: Styling for the images to make them visually distinct (for testing purposes) */
    .square {
      aspect-ratio: 1 / 1;
    }
    .rectangle {
      aspect-ratio: 16 / 9;
    }
  </style>
</head>
<body>
  <div class="image-grid">
    <img src="images/Utah_state.png" alt="Square Image 1" class="square">
    <img src="images/WA_State.png" alt="Rectangle Image 1" class="rectangle">
    <img src="images/Montana_state.png" alt="Square Image 2" class="square">
    <img src="images/Idaho_State.jpg" alt="Rectangle Image 2" class="rectangle">
  </div>
</body>
</html>

# {% include icon.html icon="fa-solid fa-users" %}Local Public Health Partners

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Healthcare Partners

## {% include icon.html icon="fa-solid fa-users" %}Intermountain Health

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: ihc" %}

## {% include icon.html icon="fa-solid fa-users" %}Pullman Regional Hospital

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: prh" %}

## {% include icon.html icon="fa-solid fa-users" %}UHealth

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: uh" %}

## {% include icon.html icon="fa-solid fa-users" %}VA 

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: va" %}


{% include section.html dark=true %}

ForeSITE aims to integrate forecasting and analytics with public health
departments and healthcare organizations regionally in the Intermountain West and nationally in
the Department of Veterans Affairs (VA).

{% include section.html %}

{% capture content %}

{% include figure.html image="images/Samore_CDC.png" %}
{% include figure.html image="images/Collingwood_CFA.png" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
