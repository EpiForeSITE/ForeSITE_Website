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
  text="Contact PI"
  link="Matthew.Samore@hsc.utah.edu"
%}
{%
  include button.html
  type="email"
  text="Program Manager"
  link="kristina.stratford@hsc.utah.edu"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/Keegan_CDC.png"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/CFAVisit.jpeg"
%}

{% endcapture %}

{% capture col3 %}

{%
  include figure.html
  image="images/Stratford_CFA.png"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

{% include section.html dark=true %}

{% capture text %}

While ForeSITE focuses on developing and implementing tools across the intermountain west, we are always excited to talk with academics and public health or healthcare partners more broadly. Please reach out for collaboration inquiries. 

{% endcapture %}

