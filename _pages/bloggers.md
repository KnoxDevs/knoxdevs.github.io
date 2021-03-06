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
      <h3 id="{{blogger.name | replace: " ", "_" | url_encode | downcase }}">{{blogger.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture image_path %}assets/cluster_images/bloggers/{{ blogger.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains image_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ blogger.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ blogger.description | strip_html }}
    </main>  
  <footer class="card__footer">
      <ul>
          {% if blogger.social.twitter %}
          <li><a href="https://twitter.com/{{ blogger.social.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if blogger.social.github %}
          <li><a href="https://github.com/{{ blogger.social.github }}" target="_blank"><img src="/assets/icons/icon-github.svg" class="icon icon-github"></a></li>
          {% endif %}
          {% if blogger.online.website %}
          <li><a href="{{ blogger.online.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
          {% if blogger.online.feed %}
          <li><a href="{{ blogger.online.feed }}" target="_blank"><img src="/assets/icons/icon-rss.svg" class="icon icon-rss"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you a local dev that would like to be featured here? Send a Pull Request to add your blog. You can see the template for groups [here](https://github.com/KnoxDevs/directory/tree/master/bloggers).
</section>
