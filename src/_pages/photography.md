---
layout: splash
permalink: /photography/
title: "Photography"
---

{% assign sorted_photos = site.photos | sort: "order" %}
<div class="photo-gallery">
<ul>
  {% for image in sorted_photos reversed %}
	{% capture img_url %}{{ image.image_path }}{% endcapture %}  <!-- Workaround to pass variables to include tags, note the lack of spaces -->
	{% capture img_caption %}{{ image.caption }}{% endcapture %}
    <li>
			{%include lightbox.html src=img_url group="abc" title=img_caption %}
    </li>
  {% endfor %}
</ul>
</div>
