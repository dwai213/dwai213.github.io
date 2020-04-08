---
title: "Projects"
permalink: /projects/
author_profile: true
---

{% include base_path %}

{% assign my_portfolio = site.portfolio | reverse %}
{% for post in  my_portfolio %}
  {% include archive-single.html %}
{% endfor %}

