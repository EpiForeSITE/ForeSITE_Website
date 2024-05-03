---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

For interest or inquiries about ForeSITE, please reach out!


{%
  include button.html
  type="email"
  text="jane@smith.com"
  link="jane@smith.com"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/Keegan_CDC.png"
  caption="Lorem ipsum"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/CFAVisit.jpeg"
  caption="CFA Site Visit"
%}

{% endcapture %}

{% capture col3 %}

{%
  include figure.html
  image="images/Stratford_CFA.png"
  caption="ForeSITE Kickoff"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

{% include section.html dark=true %}

{% capture text %}

While ForeSITE focuses on developing and implementing tools across the intermountain west, we are always excited to talk with academics and public health or healthcare partners more broadly. Please reach out for collaboration inquiries. 

{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
