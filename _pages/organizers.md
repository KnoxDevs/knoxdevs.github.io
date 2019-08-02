<!-- Get just the last name followed by the full name so that we can sort by last name, which is typically how sorting is done-->
{%- capture organizer_lastname_name -%}
    {%- for organizers_array in site.data.organizers -%}
       {{ organizers_array[1] | map: 'name' | split: ' ' | last | remove: '"]' | escape }}, {{ organizers_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_lastname_name = organizer_lastname_name | split: ' |' | sort_natural %}
<!-- Get just the last name -->
{%- capture organizer_lastname -%}
    {%- for organizers_array in site.data.organizers -%}
       {{ organizers_array[1] | map: 'name' | split: ' ' | last | remove: '"]' | escape }}, |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_lastname = organizer_lastname | split: '|' | sort_natural %}
<!-- Get the full names by subtraction. Really. -->
{%- capture sorted_organizers -%}
    {%- for name in sorted_lastname_name -%}
            {{ name | replace: sorted_lastname[forloop.index0], ''}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted = sorted_organizers | split: ' |' %}
<!-- Now make the cards -->
<section class="cards">
{% for organizer_name in sorted %}
{% assign organizers = site.data.organizers | where:'name',organizer_name %}
{% assign organizer = organizers[0] %}
<article class="card">
    <header class="card__title">
      <h3 id="{{organizer.name | replace: " ", "_" | url_encode | downcase }}">{{organizer.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture image_path %}assets/cluster_images/organizers/{{ organizer.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains image_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ organizer.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ organizer.description | strip_html }}
    </main>
  <footer class="card__footer">
    {% if organizer.group %}
        {% for group in organizer.group %}
            {% if group contains "KnoxDevs" %}
                {% if forloop.last == true %}
                    <small>{{group}} Organizer</small>
                {% else %}
                    <small>{{group}}, </small>
                {% endif %}
            {% else %}
                {% if forloop.last == true %}
                    <small><a href = "{{absolute.url}}/groups/#{{ group | replace: " ", "_" | url_encode | downcase }}">{{group}}</a> Organizer</small>
                {% else %}
                    <small><a href = "{{absolute.url}}/groups/#{{ group | replace: " ", "_" | url_encode | downcase }}">{{group}}</a>, </small>
                {% endif %}
            {% endif %}
        {% endfor %}
    {% endif %}
      <ul>
          {% if organizer.links.github %}
          <li><a href="https://github.com/{{ organizer.links.github }}" target="_blank"><img src="/assets/icons/icon-github.svg" class="icon icon-github"></a></li>
          {% endif %}
          {% if organizer.links.twitter %}
          <li><a href="https://twitter.com/{{ organizer.links.twitter }}" target="_blank"><img src="/assets/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organizer.links.website %}
          <li><a href="http://{{ organizer.links.website }}" target="_blank"><img src="/assets/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>