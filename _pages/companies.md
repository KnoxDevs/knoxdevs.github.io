---
title: Companies
layout: default
permalink: "/companies/"
---
## {{page.title}}

Knoxville is home to a variety of companies that employ a wide ranging talent of software developers of all ages, backgrounds, and experiences. Below is a list of active companies that not only employ great people, but are active in the community as well. Some even support meetups here locally.

<hr/>
<section class="cards">
{% assign companies = site.companies | sort: 'name' %}
{% for company in companies %}
<article class="card">
    <header class="card__title">
      <h3>{{company.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{company.image}}">
    </figure>
    <main class="card__description">
        {{ company.content | strip_html | truncatewords:50 }}
    </main>  
    <footer class="card__footer">
        Last updated {{company.date_updated | date: '%B %Y' }}
      <ul>
          {% if company.online.twitter %}
          <li><a href="https://twitter.com/{{ company.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if company.online.website %}
          <li><a href="{{ company.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if company.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{company.location.name}}"><a href="https://goo.gl/maps/{{ company.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local company that employs local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you work for a company that you don't see listed here? Send a Pull Request to add your company. You can see the template for companies [here](#).

</section>