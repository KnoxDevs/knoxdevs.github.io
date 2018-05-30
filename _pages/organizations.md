---
title: Organizations
layout: default
permalink: "/organizations/"
---
## {{page.title}}

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
        {{ organization.content | strip_html | truncatewords:50 }}
    </main>  
    <footer class="card__footer">
        Last updated {{organization.date_updated | date: '%B %Y' }}
      <ul>
          {% if organization.online.twitter %}
          <li><a href="https://twitter.com/{{ organization.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organization.online.website %}
          <li><a href="{{ organization.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if organization.location.gmap %}
          <li data-toggle="tooltip" data-placement="bottom" title="{{organization.location.name}}"><a href="https://goo.gl/maps/{{ organization.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local organization that employs local software developers and would like to be involved in Knoxville' software developer community? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you work for a organization that you don't see listed here? Send a Pull Request to add your organization. You can see the template for organizations [here](#).

</section>