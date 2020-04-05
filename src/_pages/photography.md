---
layout: archive
permalink: /photography/
title: "Photography"
author_profile: true
---

{% assign sorted_photos = site.photos | sort: "order" %}
<ul class="photo-gallery">
  {% for image in sorted_photos reversed %}
    <li> <a href="{{ image.image_path }}" data-lightbox="wow" data-title="{{ image.caption }}">
            <img src="{{ image.image_path }}" alt="{{ image.title }}"/></a>
    </li>
  {% endfor %}
</ul>