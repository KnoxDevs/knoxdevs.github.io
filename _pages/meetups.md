---
title: Meetups
layout: default
permalink: "/meetups/"
---
## {{page.title}}

Knoxville is home to a variety of meetups that cater to the robust software developer community of all ages, backgrounds, and experiences. Below is a list of active meetups that both meet in person and have active discussions online in one of our many slack channels. 

<hr>
<section class="cards">
{% assign meetups = site.meetups | sort: 'name' %}
{% for meetup in meetups %}
<article class="card">
    <header class="card__title">
      <h3>{{meetup.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{meetup.image}}">
    </figure>
    <main class="card__description">
        {{ meetup.content | strip_html | truncatewords:50 }}
    </main>  
    <footer class="card__footer">
        Last updated {{meetup.date_updated | date: '%B %Y' }}
        <ul>
            {% if meetup.online.github %}
            <li>
                <a href="https://github.com/{{ meetup.online.github }}" target="_blank"><img src="/assets/images/icon-github.svg" class="icon icon-github"></a>
            </li>
            {% endif %}
            {% if meetup.online.meetup %}
            <li>
                <a href="https://meetup.com/{{ meetup.online.meetup }}" target="_blank">
                    <img src="/assets/images/icon-meetup.svg" class="icon icon-meetup">
                </a>
            </li>
            {% endif %}
            {% if meetup.online.twitter %}
            <li>
                <a href="https://twitter.com/{{ meetup.online.twitter }}" target="_blank">
                    <img src="/assets/images/icon-twitter.svg" class="icon icon-twitter">
                </a>
            </li>
            {% endif %}
            {% if meetup.online.website %}
            <li>
                <a href="{{ meetup.online.website }}" target="_blank">
                <img src="/assets/images/icon-link.svg" class="icon icon-website">
                </a>
            </li>
            {% endif %}
            {% if meetup.location.gmap %}
            <li data-toggle="tooltip" data-placement="bottom" title="{{meetup.location.name}}">
                <a href="https://goo.gl/maps/{{ meetup.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location">
                </a>
            </li>
            {% endif %}
        </ul>
    </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you an existing meetup organizer? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you not see your group here? Send a Pull Request to add your group listing. You can see the template for groups [here](#).

</section>