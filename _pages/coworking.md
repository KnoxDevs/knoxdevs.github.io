---
title: Coworking
layout: default
permalink: "/coworking/"
---
## {{page.title}}

Knoxville is home to a variety of coworking spaces that provide a place to work - of all sizes - for a wide range of talented software developers of all ages, backgrounds, and experiences. Below is a list of active coworking spaces that not only provide an office to great people here in Knoxville, but are active in providing meeting space to the community as well.

<hr>
<!-- Ensure that spaces are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture coworking_name -%}
    {%- for spaces_array in site.data.coworking -%}
       {{ spaces_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_coworkingname = coworking_name | split: ' |' | sort_natural %}

<section class="cards">
{% for coworking_name in sorted_coworkingname %}
{% assign spaces = site.data.coworking | where:'name',coworking_name %}
{% assign coworking = spaces[0] %}
<article class="card">
    <header class="card__title">
      <h3 id = "{{cowork_space.name | url_encode }}" >{{cowork_space.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{cowork_space.image}}">
    </figure>
    <main class="card__description">
        {{ cowork_space.content | strip_html | truncatewords:50 }}
    </main>  
  <footer class="card__footer">
      Last updated {{cowork_space.date_updated | date: '%B %Y' }}
      <ul>
          {% if cowork_space.online.twitter %}
          <li><a href="https://twitter.com/{{ cowork_space.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if cowork_space.online.website %}
          <li><a href="{{ cowork_space.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if cowork_space.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{cowork_space.location.name}}"><a href="https://goo.gl/maps/{{ cowork_space.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local coworking space that provides a coworking locations for local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you work at a space that you don't see listed here? Send a Pull Request to add your cowork_space. You can see the template for coworking spaces [here](#).

</section>