---
title: Developers
layout: default
permalink: "/developers/"
---
## {{page.title}}

Knoxville is home to a variety of software developers, many of whom also blog! Below is a snapshot of developers in the area.

<hr />
<section class="cards">
{% assign developers = site.developers | sort: 'name' %}
{% for developer in developers %}
<article class="card">
    <header class="card__title">
      <h3>{{developer.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{developer.image}}">
    </figure>
    <main class="card__description">
        {{ developer.content | strip_html | truncatewords:50 }}
    </main>  
  <footer class="card__footer">
      Last updated {{developer.date_updated | date: '%B %Y' }}
      <ul>
          {% if developer.online.twitter %}
          <li><a href="https://twitter.com/{{ developer.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if developer.online.website %}
          <li><a href="{{ developer.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local dev that would like to be featured here? You can update the listing here by sending a Pull Request with an individual markdown file [here](#). Follow the template and send the request!

Do you know of a blog that should be listed here? Send a Pull Request to add them! You can see the template for developers developers [here](#).

</section>