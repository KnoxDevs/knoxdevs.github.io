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
      <h3 id="{{organizer.name | url_encode}}">{{organizer.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{organizer.image}}">
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
                    <small><a href = "{{absolute.url}}/groups/#{{ group | url_encode }}">{{group}}</a> Organizer</small>
                {% else %}
                    <small><a href = "{{absolute.url}}/groups/#{{ group | url_encode }}">{{group}}</a>, </small>
                {% endif %}
            {% endif %}
        {% endfor %}
    {% endif %}
      <ul>
          {% if organizer.social.github %}
          <li><a href="https://github.com/{{ organizer.social.github }}" target="_blank"><img src="/assets/images/icons/icon-github.svg" class="icon icon-github"></a></li>
          {% endif %}
          {% if organizer.social.twitter %}
          <li><a href="https://twitter.com/{{ organizer.social.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organizer.online.website %}
          <li><a href="http://{{ organizer.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>