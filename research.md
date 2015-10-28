---
layout: page
title: research
permalink: /research/
---

Dennis's research interests lies in robotics, mechatronics, and control. For a list of his publications, see his [CV]({{ site.baseurl }}/static/files/cv.pdf)

## Particle Filter
---

I worked with Yizhou Wang on attitude estimation through particle filters, a Monte Carlo method for stochastic estimation. The big idea here is to represent a state distribution for a system's states by instantiating many particles that represents all of the states the system can be. Using Baye's rule and sensor measurements, we can selectively breed/multiply the particles that probabilistically more accurately reflect the true state.
In marginalized particle filters, we take advantage of the linear structure in the system to save computation when we propagate the particles supporting the state distribution. Our work is summarized in our conference paper [here]({{ site.baseurl }}/static/files/DSCC14PF.pdf) and my presentation at DSCC 2014 can be found [here]({{ site.baseurl }}/static/files/dscc2014_ssmpf.pdf). For a slightly more in depth explanation of particle filters, you can read more [here]({{ site.baseurl }}/static/files/pf_overview.pdf).

<div class="slick-slider-small">
	<div class="multiple-items">
	  <div><img src="{{ site.baseurl }}/static/research/mpf1.png" alt="Particle Filter"> </div>
	  <div><img src="{{ site.baseurl }}/static/research/mpf2.png" alt="Particle Filter"> </div>
	  <div><img src="{{ site.baseurl }}/static/research/mpf3.png" alt="Particle Filter"> </div>
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
</div>

<br><br>

##  Tailbot 
---

<div class="img_row">
	<img class="contain_col two" src="{{ site.baseurl }}/static/research/tail1.jpg" alt="" title="Tailbot with an agama lizard"/>
	<img class="contain_col one" src="{{ site.baseurl }}/static/research/tail2.jpg" alt="" title="Tailbot without its racing cover"/>
</div>
<div class="col three caption">
	Tailbot alongside a lizard on the left. Tailbot without its racing cover on the right.
</div>

Tailbot became quite a celebrity in the robotics world because it demonstrated the insight biologists have gleaned from lizards. Lizards have an ability to right themselves in midair by actively using their tail to control its angular momentum. It was featured on the front cover of an edition of [Nature](http://www.nature.com/nature/journal/v481/n7380/full/nature10710.html) and made headlines for [UC Berkeley's newcenter](http://newscenter.berkeley.edu/2012/01/04/leaping-lizards-show-robots-the-value-of-a-tail/). Tailbot was the first robot in my career and I heavily contributed to its mechatronics design.

<div class="img_row">
	<img class="col one" src="{{ site.baseurl }}/static/research/tail3.jpg" alt="" title="Tailbot's electronics'"/>
	<iframe class="col one" width="480" height="360" src="https://www.youtube.com/embed/s2Lk_2YCtA4" frameborder="0" allowfullscreen></iframe>
	<img class="col one" src="{{ site.baseurl }}/static/research/tail4.jpg" alt="" title="Tailbot v2 with mobile chassis"/>
</div>
<div class="col three caption">
	From left to right: tailbot's electronic system, tailbot self-righting abilities, and second generation of tailbot on a mobile platform
</div>

<br><br>

## Rehabilitation
---
In classical gait rehabilitation therapy, there is no quantitative approach to base a diagnosis. Instead, much of therapy for a patient afflicted with a gait disorder is based on a therapist’s physical observations and intuition. More often than not, the level of care is proportional to the therapist’s experience. In addition, for patients with a gait disorder, it is often difficult to physically transport themselves to receive therapy as well. As a result, we created a system where a patient will wear a series of intelligently placed sensor nodes that will record Euler angles and transfer it wirelessly to a local computer, which will then transfer it via Internet to the therapist’s computer.

<div class="img_row">
	<iframe class="col one" width="480" height="360" src="https://www.youtube.com/embed/QdeaxMw0Gmk" frameborder="0" allowfullscreen></iframe>
	<img class="contain_col one" src="{{ site.baseurl }}/static/research/rehab.png" alt="" title="Flowchart for networked rehabilitation'"/>
	<iframe class="col one" width="480" height="360" src="https://www.youtube.com/embed/NgY4rWWbm3k" frameborder="0" allowfullscreen></iframe>
</div>
<div class="col three caption">
	From left to right: video of sensor readings mapped to a shoe in LabVIEW, flowchart for networked rehabilitation, and video of a sensor test on the leg
</div>

With Kevin Haninger, I worked on developing the software required to calculate the Euler angles in Arduino using [Varesano’s FreeIMU library](http://www.varesano.net/projects/hardware/FreeIMU) and packet loss compensation and visualization in LabVIEW. Each sensor node on the patient calculates Euler angles in the onboard Arduino. When prompted by the local computer, the Arduino will respond and return a set of measurements to the local computer, where LabVIEW will parse it and process the data into useful information. We have since published our work into a conference paper at the 2012 IEEE/ASME International Conference on Advanced Intelligent Mechatronics and can be found [here](static/files/rehab.pdf).

