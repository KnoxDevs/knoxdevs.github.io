---
layout: single
title: About
permalink: /about/
last_modified_at: 2018-05-29T16:00:00-04:00
---
KnoxDevs is a registered non-profit organization whose sole mission is to foster a healthy software developer community in Knoxville, TN.

## Code of Conduct

### Our Pledge
KnoxDevs is dedicated to providing an outstanding experience, to increase learning opportunities for all our members, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, sexual identity, or sexual orientation.

We do not tolerate harassment of members in any form, and we would like to take this opportunity to remind all members that KnoxDevs was founded on: passionate, but respectful dialog between our members, for our members. Please treat your fellow members with respect!

Harassment<sup>[1](#fn1)</sup> is not appropriate for any group venue. Group members violating these rules may be sanctioned or expelled from the group, at the discretion of the group organizers.

Members must remember that KnoxDevs organizers and volunteers are not trained conflict resolution specialists, nor are they security or law enforcement. KnoxDevs organizers and volunteers will immediately escalate issues around safety, violence, or similar situations to the Knoxville Police Department.

For the protection of both members and our organization, KnoxDevs will never put its organizers or volunteers in the position of trying to assess whether or not an incident merits reporting. If there is any doubt, we will report incidents to the Knoxville Police Department immediately.

### Incident Resolution
Members should follow the golden rule: “One should treat others as one would like others to treat oneself.” Treat other members with respect. Simple disagreements should be resolved between the individuals concerned. Harassment or more serious issues should be escalated to a KnoxDevs organizer. That organizer will immediately contact a KnoxDevs Board member who has the responsibility to assist in resolution.

><a name="fn1">1</a>: Examples include offensive comments, verbal threats or demands, sexualized images in public spaces, intimidation, stalking, harassing photography or recording, sustained disruption of sessions or events, unwelcome physical contact or sexual attention, and the advocating or encouragement of any of the above behavior.

## Organizers
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
        {{ organizer.blurb | strip_html | truncatewords:50 }}
    </main>
  <footer class="card__footer">
    {% if organizer.group %}
        <small> {{organizer.group | join: ', '}} Organizer</small>
    {% endif %}
      <ul>
          {% if organizer.online.github %}
          <li><a href="https://github.com/{{ organizer.online.github }}" target="_blank"><img src="/assets/images/icons/icon-github.svg" class="icon icon-github"></a></li>
          {% endif %}
          {% if organizer.online.twitter %}
          <li><a href="https://twitter.com/{{ organizer.online.twitter }}" target="_blank"><img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if organizer.online.website %}
          <li><a href="http://{{ organizer.online.website }}" target="_blank"><img src="/assets/images/icons/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>
