---
layout: splash
permalink: /photography/
title: "Photography"
---

{% assign sorted_photos = site.photos | sort: "order" %}
<ul class="photo-gallery">
  {% for image in sorted_photos reversed %}
    <li> <a href="{{ image.image_path }}" data-title="{{ image.caption }}">
            <img src="{{ image.image_path }}" alt="{{ image.title }}"/></a>
    </li>
  {% endfor %}
</ul>