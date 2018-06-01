---
title: Bloggers
layout: default
permalink: "/bloggers/"
---
## {{page.title}}

Knoxville is home to a variety of software devs, many of whom also blog! Below is a snapshot of bloggers in the area.

<hr />
<!-- Get just the last name followed by the full name so that we can sort by last name, which is typically how sorting is done-->
{%- capture blogger_lastname_name -%}
    {%- for bloggers_array in site.data.bloggers -%}
       {{ bloggers_array[1] | map: 'name' | split: ' ' | last | remove: '"]' | escape }}, {{ bloggers_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_lastname_name = blogger_lastname_name | split: ' |' | sort_natural %}
<!-- Get just the last name -->
{%- capture blogger_lastname -%}
    {%- for bloggers_array in site.data.bloggers -%}
       {{ bloggers_array[1] | map: 'name' | split: ' ' | last | remove: '"]' | escape }}, |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_lastname = blogger_lastname | split: '|' | sort_natural %}
<!-- Get the full names by subtraction. Really. -->
{%- capture sorted_bloggers -%}
    {%- for name in sorted_lastname_name -%}
            {{ name | replace: sorted_lastname[forloop.index0], ''}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted = sorted_bloggers | split: ' |' %}
<!-- Now make the cards -->
<section class="cards">
{% for blogger_name in sorted %}
{% assign bloggers = site.data.bloggers | where:'name',blogger_name %}
{% assign blogger = bloggers[0] %}
<article class="card">
    <header class="card__title">
      <h3>{{blogger.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{blogger.image}}">
    </figure>
    <main class="card__description">
        {{ blogger.content | strip_html | truncatewords:50 }}
    </main>  
  <footer class="card__footer">
      Last updated {{blogger.date_updated | date: '%B %Y' }}
      <ul>
          {% if blogger.online.twitter %}
          <li><a href="https://twitter.com/{{ blogger.online.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if blogger.online.website %}
          <li><a href="{{ blogger.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local dev that would like to be featured here? You can update the listing here by sending a Pull Request with an individual markdown file [here](#). Follow the template and send the request!

Do you know of a blog that should be listed here? Send a Pull Request to add them! You can see the template for bloggers bloggers [here](#).

</section>