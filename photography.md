---
layout: page
title: photography
permalink: /photography/
---

<div class="multiple-items">
    <div> <img src="{{ site.baseurl }}/static/01.png" alt="Hong Kong from Victoria Peak"> </div>
    <div> <img src="{{ site.baseurl }}/static/02.png" alt="Egg and toast with coffee"> </div>
    <div> <img src="{{ site.baseurl }}/static/03.png" alt="Yehliu Geological Park, Taiwan"> </div>
</div>

<script type="text/javascript">
$(document).ready(function(){
  $('.multiple-items').slick({
  dots: true,
  infinite: false,
  slidesToShow: 1,
  slidesToScroll: 1,
  });
});
</script>