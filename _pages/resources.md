---
title: Resources
layout: default
permalink: "/resources/"
---
## {{page.title}}

Are you a group organizer? Are you a software developer looking for help to organize something great? We have put together a list of resources to help you navigate Knoxville:

- great [organizations](#organizations) that often support developers
- superb [regional conferences](#conferences)
- awesome [coworking spots](#coworking_spaces)
- the perfect [spaces to host events](#event_spaces).

<h2 id="organizations">Organizations</h2>

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
      <h3 id="{{ organization.name | replace: " ", "_" | url_encode | downcase }}">{{organization.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture logo_path %}assets/cluster_images/organizations/{{ organization.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains logo_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ organization.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ organization.description | strip_html }}
    </main>  
    <footer class="card__footer">
      <ul>
          {% if organization.social.twitter %}
          <li><a href="https://twitter.com/{{ organization.social.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organization.social.facebook %}
          <li><a href="https://facebook.com/{{ organization.social.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if organization.online.website %}
          <li><a href="{{ organization.online.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if organization.location.address %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{organization.location.name}}"><a href="https://www.google.com/maps/place/{{ organization.location.address | url_encode }}" target="_blank"><img src="/assets/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_organizations" markdown="1">
Are you (or do you work for) a local organization that employs local software developers and would like to be involved in Knoxville' software developer community? Or You can update the listing here by sending a Pull Request to the individual markdown file [here](https://github.com/KnoxDevs/directory/tree/master/organizations).
</section>

<h2 id="conferences">Conferences</h2>

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
      <h3 id="{{ conference.name | replace: " ", "_" | url_encode | downcase }}">{{conference.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture logo_path %}assets/cluster_images/conferences/{{ conference.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains logo_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ conference.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
      {{ conference.description | strip_html }}
    </main>  
    <footer class="card__footer">
        <ul>
          {% if conference.social.twitter %}
          <li><a href="https://twitter.com/{{ conference.social.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if conference.social.facebook %}
          <li><a href="https://facebook.com/{{ conference.social.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if conference.online.website %}
          <li><a href="{{ conference.online.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if conference.location.address %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{conference.location.name}}"><a href="https://www.google.com/maps/place/{{ conference.location.address | url_encode }}" target="_blank"><img src="/assets/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
        </ul>
    </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_conferences" markdown="1">
Are you (or do you attend) a regional conference that you feel developers in Knoxville would be interested in attending? You can update the listing here by sending a Pull Request to the individual markdown file [here](https://github.com/KnoxDevs/directory/tree/master/conferences).
</section>

<h2 id="coworking_spaces">Coworking Spaces</h2>

Knoxville is home to a variety of event spaces that provide a place to work - of all sizes - for a wide range of talented software developers of all ages, backgrounds, and experiences. Below is a list of active event spaces that not only provide an office to great people here in Knoxville, but are active in providing meeting space to the community as well.

<hr>
<!-- Ensure that spaces are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture coworking_space_name -%}
    {%- for spaces_array in site.data.coworking_spaces -%}
       {{ spaces_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_coworking_space_name = coworking_space_name | split: ' |' | sort_natural %}

<section class="cards">
{% for coworking_space_name in sorted_coworking_space_name %}
{% assign cowork_spaces = site.data.coworking_spaces | where:'name',coworking_space_name %}
{% assign cowork_space = cowork_spaces[0] %}
<article class="card">
    <header class="card__title">
      <h3 id="{{ cowork_space.name | replace: " ", "_" | url_encode | downcase }}">{{cowork_space.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture logo_path %}assets/cluster_images/coworking_spaces/{{ cowork_space.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains logo_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ cowork_space.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ cowork_space.description | strip_html }}
    </main>  
  <footer class="card__footer">
      <ul>
          {% if cowork_space.social.twitter %}
          <li><a href="https://twitter.com/{{ cowork_space.social.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if cowork_space.social.facebook %}
          <li><a href="https://facebook.com/{{ cowork_space.social.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if cowork_space.online.website %}
          <li><a href="{{ cowork_space.online.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if cowork_space.location.address %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{cowork_space.location.name}}"><a href="https://www.google.com/maps/place/{{ cowork_space.location.address | url_encode }}" target="_blank"><img src="/assets/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_event" markdown="1">
Are you a local event space (or do you regularly work at one) that provides a event locations for local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](https://github.com/KnoxDevs/directory/tree/master/coworking_spaces).

</section>

<h2 id="event_spaces">Event Spaces</h2>

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
      <h3 id="{{ event_space.name | replace: " ", "_" | url_encode | downcase }}">{{event_space.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture logo_path %}assets/cluster_images/event_spaces/{{ event_space.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains logo_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ event_space.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ event_space.description | strip_html }}
    </main>  
  <footer class="card__footer">
      <ul>
          {% if event_space.social.twitter %}
          <li><a href="https://twitter.com/{{ event_space.social.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if event_space.organization.facebook %}
          <li><a href="https://facebook.com/{{ event_space.social.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if event_space.online.website %}
          <li><a href="http://{{ event_space.online.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if event_space.location.address %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{event_space.location.name}}"><a href="https://www.google.com/maps/place/{{ event_space.location.address | url_encode }}" target="_blank"><img src="/assets/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_event" markdown="1">
Are you a local event space (or do you regularly use one) that provides an event location for local software developers and would like to be involved in Knoxville's software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](https://github.com/KnoxDevs/directory/tree/master/event_spaces).

</section>