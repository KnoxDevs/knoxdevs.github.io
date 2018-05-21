---
title: Conferences
layout: default
permalink: "/conferences/"
---
## {{page.title}}

The Southeast is home to a variety of conferences that often feature the talent groomed here in Knoxville. Below is a list of active conferences that not only are often attended by developers here in Knoxville, but have featured speakers from Knoxville as well.

<hr>
<section class="cards">
{% assign conferences = site.conferences | sort: 'name' %}
{% for conference in conferences %}
<article class="card">
    <header class="card__title">
      <h3>{{conference.name}}</h3>
    </header>
    <figure class="card__image">
      <img src="{{conference.image}}">
    </figure>
    <main class="card__description">
      {{ conference.content | strip_html | truncatewords:50 }}
    </main>  
    <footer class="card__footer">
        Last updated {{conference.date_updated | date: '%B %Y' }}
        <ul>
          {% if conference.online.twitter %}
          <li><a href="https://twitter.com/{{ conference.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if conference.online.website %}
          <li><a href="{{ conference.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if conference.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{conference.location.name}}"><a href="https://goo.gl/maps/{{ conference.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
        </ul>
    </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a regional conference that you feel developers in Knoxville would be interested in attending? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you regularly attend a Southeast conference that you don't see listed here? Send a Pull Request to add your favortie conference. You can see the template for conferences [here](#).

</section>