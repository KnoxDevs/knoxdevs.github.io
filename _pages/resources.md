---
title: Resources
layout: default
permalink: "/resources/"
---
## {{page.title}}

Are you a group organizer? Are you a software developer looking for help to organize something great? We have put together a list of resources to help you navigate Knoxville:

- great [organizations](#Organizations) that often support developers
- superb [regional conferences](#Conferences)
- awesome [event spots](#Event+Spaces)
- the perfect [spaces to host events](#Event+Spaces).

<h2 id="Organizations">Organizations</h2>

Knoxville is home to a variety of organizations that help support local software developers through various programs they offer. Below is a list of active organizations that are active in the community. Some even support meetups here locally.

<hr>
<!-- Ensure that organizations are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture organization_name -%}
    {%- for organizations_array in site.data.organizations -%}
       {{ organizations_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_organizationname = organization_name | split: ' |' | sort_natural %}

<section class="cards">
{% for organization_name in sorted_organizationname %}
{% assign organizations = site.data.organizations | where:'name',organization_name %}
{% assign organization = organizations[0] %}
<article class="card">
    <header class="card__title">
      <h3 id="{{organization.name | url_encode }}">{{organization.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{organization.image}}">
    </figure>
    <main class="card__description">
        {{ organization.blurb | strip_html | truncatewords:50 }}
    </main>  
    <footer class="card__footer">
      <ul>
          {% if organization.online.twitter %}
          <li><a href="https://twitter.com/{{ organization.online.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organization.online.website %}
          <li><a href="{{ organization.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if organization.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{organization.location.name}}"><a href="https://goo.gl/maps/{{ organization.location.gmap }}" target="_blank"><img src="/assets/images/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_organizations" markdown="1">
Are you (or do you work for) a local organization that employs local software developers and would like to be involved in Knoxville' software developer community? Or You can update the listing here by sending a Pull Request to the individual markdown file [here]({{ site.github.repository_url }}/tree/master/{{ page.relative_path }}_data/organizations).
</section>

<h2 id="Conferences">Conferences</h2>

The Southeast is home to a variety of conferences that often feature the talent groomed here in Knoxville. Below is a list of active conferences that not only are often attended by developers here in Knoxville, but have featured speakers from Knoxville as well.

<hr>
<!-- Ensure that conferences are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture conference_name -%}
    {%- for conferences_array in site.data.conferences -%}
       {{ conferences_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_conferencename = conference_name | split: ' |' | sort_natural %}

<section class="cards">
{% for conference_name in sorted_conferencename %}
{% assign conferences = site.data.conferences | where:'name',conference_name %}
{% assign conference = conferences[0] %}
<article class="card">
    <header class="card__title">
      <h3>{{conference.name}}</h3>
    </header>
    <figure class="card__image">
      <img src="{{conference.image}}">
    </figure>
    <main class="card__description">
      {{ conference.blurb | strip_html | truncatewords:50 }}
    </main>  
    <footer class="card__footer">
        <ul>
          {% if conference.online.twitter %}
          <li><a href="https://twitter.com/{{ conference.online.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if conference.online.website %}
          <li><a href="{{ conference.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if conference.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{conference.location.name}}"><a href="https://goo.gl/maps/{{ conference.location.gmap }}" target="_blank"><img src="/assets/images/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
        </ul>
    </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_conferences" markdown="1">
Are you (or do you attend) a regional conference that you feel developers in Knoxville would be interested in attending? You can update the listing here by sending a Pull Request to the individual markdown file [here]({{ site.github.repository_url }}/tree/master/{{ page.relative_path }}_data/conferences).
</section>

<h2 id="Event+Spaces">Event Spaces</h2>

Knoxville is home to a variety of event spaces that provide a place to work - of all sizes - for a wide range of talented software developers of all ages, backgrounds, and experiences. Below is a list of active event spaces that not only provide an office to great people here in Knoxville, but are active in providing meeting space to the community as well.

<hr>
<!-- Ensure that spaces are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture event_name -%}
    {%- for spaces_array in site.data.event -%}
       {{ spaces_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_eventname = event_name | split: ' |' | sort_natural %}

<section class="cards">
{% for event_name in sorted_eventname %}
{% assign cowork_spaces = site.data.event | where:'name',event_name %}
{% assign cowork_space = cowork_spaces[0] %}
<article class="card">
    <header class="card__title">
      <h3 id = "{{cowork_space.name | url_encode }}" >{{cowork_space.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{cowork_space.image}}">
    </figure>
    <main class="card__description">
        {{ cowork_space.blurb | strip_html | truncatewords:50 }}
    </main>  
  <footer class="card__footer">
      <ul>
          {% if cowork_space.online.twitter %}
          <li><a href="https://twitter.com/{{ cowork_space.online.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if cowork_space.online.website %}
          <li><a href="{{ cowork_space.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if cowork_space.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{cowork_space.location.name}}"><a href="https://goo.gl/maps/{{ cowork_space.location.gmap }}" target="_blank"><img src="/assets/images/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_event" markdown="1">
Are you a local event space (or do you regularly work at one) that provides a event locations for local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here]({{ site.github.repository_url }}/tree/master/{{ page.relative_path }}_data/event).

</section>

<h2 id="Event+Spaces">Event Spaces</h2>

Knoxville is home to a variety of event spaces that provide a place to work - of all sizes - for a wide range of talented software developers of all ages, backgrounds, and experiences. Below is a list of active event spaces that not only provide an office to great people here in Knoxville, but are active in providing meeting space to the community as well.

<hr>
<!-- Ensure that spaces are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture event_space_name -%}
    {%- for spaces_array in site.data.event_spaces -%}
       {{ spaces_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_event_spacename = event_space_name | split: ' |' | sort_natural %}

<section class="cards">
{% for event_space_name in sorted_event_spacename %}
{% assign event_spaces = site.data.event_spaces | where:'name',event_space_name %}
{% assign event_space = event_spaces[0] %}
<article class="card">
    <header class="card__title">
      <h3 id = "{{event_space.name | url_encode }}" >{{event_space.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{event_space.image}}">
    </figure>
    <main class="card__description">
        {{ event_space.blurb | strip_html | truncatewords:50 }}
    </main>  
  <footer class="card__footer">
      <ul>
          {% if event_space.online.twitter %}
          <li><a href="https://twitter.com/{{ event_space.online.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if event_space.online.website %}
          <li><a href="{{ event_space.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if event_space.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{event_space.location.name}}"><a href="https://goo.gl/maps/{{ event_space.location.gmap }}" target="_blank"><img src="/assets/images/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_event" markdown="1">
Are you a local event space (or do you regularly use one) that provides an event location for local software developers and would like to be involved in Knoxville's software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here]({{ site.github.repository_url }}/tree/master/{{ page.relative_path }}_data/event_spaces).

</section>