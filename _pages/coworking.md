---
title: Coworking
layout: default
permalink: "/coworking/"
---
## {{page.title}}

Knoxville is home to a variety of coworking spaces that provide a place to work - of all sizes - for a wide range of talented software developers of all ages, backgrounds, and experiences. Below is a list of active coworking spaces that not only provide an office to great people here in Knoxville, but are active in providing meeting space to the community as well.

<hr>
<section class="cards">
{% assign coworking = site.coworking | sort: 'name' %}
{% for space in coworking %}
<article class="card">
    <header class="card__title">
      <h3>{{space.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{space.image}}">
    </figure>
    <main class="card__description">
        {{ space.content | strip_html | truncatewords:50 }}
    </main>  
  <footer class="card__footer">
      Last updated {{space.date_updated | date: '%B %Y' }}
      <ul>
          {% if space.online.twitter %}
          <li><a href="https://twitter.com/{{ space.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if space.online.website %}
          <li><a href="{{ space.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if space.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{space.location.name}}"><a href="https://goo.gl/maps/{{ space.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local coworking space that provides a coworking locations for local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you work at a space that you don't see listed here? Send a Pull Request to add your space. You can see the template for coworking spaces [here](#).

</section>