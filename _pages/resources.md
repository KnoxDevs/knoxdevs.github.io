---
title: Resources
layout: default
permalink: "/resources/"
---
## {{page.title}}

Are you a group organizer? Are you a software developer looking for help to organize something great? We have put together a list of resources to help you navigate Knoxville:

- great [organizations](#organizations) that often support developers
- superb [regional conferences](#conferences)
- awesome [coworking spots or places to host events](#spaces)

<h2 id="organizations">Organizations</h2>

Knoxville is home to a variety of organizations that help support local software developers through various programs they offer. Below is a list of active organizations that are active in the community. Some even support meetups here locally.

<hr>
<!-- Ensure that organizations are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture organization_name -%}
    {%- for organizations_array in site.data.organizations -%}
        {%- if organizations_array[1].name != "template" -%}
       {{ organizations_array[1] | map: 'name'}} |
        {%- endif -%}
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
          {% if organization.links.twitter %}
          <li><a href="https://twitter.com/{{ organization.links.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organization.links.facebook %}
          <li><a href="https://facebook.com/{{ organization.links.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if organization.links.website %}
          <li><a href="{{ organization.links.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
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
        {%- if conferences_array[1].name != "template" -%}
       {{ conferences_array[1] | map: 'name'}} |
        {%- endif -%}
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
          {% if conference.links.twitter %}
          <li><a href="https://twitter.com/{{ conference.links.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if conference.links.facebook %}
          <li><a href="https://facebook.com/{{ conference.links.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if conference.links.website %}
          <li><a href="{{ conference.links.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
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

<h2 id="spaces">Coworking Spaces and Event Spaces</h2>

Knoxville is home to a variety of event spaces that provide a place to work - of all sizes - for a wide range of talented software developers of all ages, backgrounds, and experiences. Below is a list of active event spaces that not only provide an office to great people here in Knoxville, but are active in providing meeting space to the community as well.

<hr>
<!-- Ensure that spaces are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture space_name -%}
    {%- for spaces_array in site.data.spaces -%}
        {%- if spaces_array[1].name != "template" -%}
       {{ spaces_array[1] | map: 'name'}} |
        {%- endif -%}
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_space_name = space_name | split: ' |' | sort_natural %}

<section class="cards">
{% for space_name in sorted_space_name %}
{% assign spaces = site.data.spaces | where:'name',space_name %}
{% assign space = spaces[0] %}
<article class="card">
    <header class="card__title">
      <h3 id="{{ space.name | replace: " ", "_" | url_encode | downcase }}">{{space.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture logo_path %}assets/cluster_images/spaces/{{ space.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains logo_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ space.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ space.description | strip_html }}
    </main>  
  <footer class="card__footer">
      <ul>
          {% if space.links.twitter %}
          <li><a href="https://twitter.com/{{ space.links.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if space.links.facebook %}
          <li><a href="https://facebook.com/{{ space.links.facebook }}" target="_blank"><img src="/assets/icons/icon-fb.svg" class="icon icon-fb"></a></li>
          {% endif %}
          {% if space.links.website %}
          <li><a href="{{ space.links.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if space.location.address %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{space.location.name}}"><a href="https://www.google.com/maps/place/{{ space.location.address | url_encode }}" target="_blank"><img src="/assets/icons/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list_space" markdown="1">
Are you a local event space (or do you regularly work at one) that provides a event locations for local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](https://github.com/KnoxDevs/directory/tree/master/spaces).

</section>
