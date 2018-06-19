---
title: Groups
layout: default
permalink: "/groups/"
---
## {{page.title}}

Knoxville is home to a variety of groups that cater to the robust software developer community of all ages, backgrounds, and experiences. Below is a list of active groups that both meet in person and have active discussions online in one of our many slack channels. 

<hr>
<!-- Ensure that groups are sorted alphabetically, not based on file name in `_data` folder -->
{%- capture group_name -%}
    {%- for groups_array in site.data.groups -%}
       {{ groups_array[1] | map: 'name'}} |
    {%- endfor -%}
{%- endcapture -%}
{% assign sorted_groupname = group_name | split: ' |' | sort_natural %}

<section class="cards">
{% for group_name in sorted_groupname %}
{% assign groups = site.data.groups | where:'name',group_name %}
{% assign group = groups[0] %}
<article class="card">
    <header class="card__title">
      <h3 id="{{group.name | replace: " ", "_" | url_encode | downcase }}">{{group.name}}</h3>
    </header>
    <figure class="card__image">
    {% capture logo_path %}assets/images/groups/{{ group.name | replace: " ", "_" | url_encode | downcase }}{% endcapture %}
    {% for image in site.static_files %}
        {% if image.path contains logo_path %}
            <img src="{{absolute.url}}{{image.path}}" alt ="{{ group.name }}"/>
        {% endif %}
    {% endfor %}
    </figure>
    <main class="card__description">
        {{ group.description | markdownify | truncatewords:50 }}
    </main> 
    <footer class="card__footer">
        {% assign organizers = site.data.organizers | where:'group',group.name %}
        {% unless organizers == empty %}
            <small class="organizers">Organized by: 
            {% for organizer in organizers %}
                {% if forloop.last == true %}
                    <a href="{{absolute.url}}/about/#{{ organizer.name | replace: " ", "_" | url_encode | downcase }}">{{organizer.name}}</a>
                {% else %}
                    <a href="{{absolute.url}}/about/#{{ organizer.name | replace: " ", "_" | url_encode | downcase }}">{{organizer.name}}</a>, 
                {% endif %}   
            {% endfor %}
        </small><br/><br/>
        {% endunless %}
        {% if group.slack_channel %}
        <img src="/assets/images/icons/icon-slack.svg" class="icon icon-slack">
        <code>
            <a href="https://knoxdevs.slack.com/messages/{{ group.slack_channel }}"  target="_blank" title="Join the conversation on the KnoxDevs slack in the {{ group.slack_channel }} channel!">#{{ group.slack_channel }}</a>
        </code>
        {% endif %}
        <ul>
            {% if group.social.github %}
            <li>
                <a href="https://github.com/{{ group.social.github }}" target="_blank"><img src="/assets/images/icons/icon-github.svg" class="icon icon-github"></a>
            </li>
            {% endif %}
            {% if group.social.meetup %}
            <li>
                <a href="https://meetup.com/{{ group.social.meetup }}" target="_blank">
                    <img src="/assets/images/icons/icon-meetup.svg" class="icon icon-meetup">
                </a>
            </li>
            {% endif %}
            {% if group.social.twitter %}
            <li>
                <a href="https://twitter.com/{{ group.social.twitter }}" target="_blank">
                    <img src="/assets/images/icons/icon-twitter.svg" class="icon icon-twitter">
                </a>
            </li>
            {% endif %}
            {% if group.online.website %}
            <li>
                <a href="{{ group.online.website }}" target="_blank">
                <img src="/assets/images/icons/icon-link.svg" class="icon icon-website">
                </a>
            </li>
            {% endif %}
            {% if group.location.address %}
            <li data-toggle="tooltip" data-placement="bottom" title="{{group.location.name}}">
                <a href="https://www.google.com/maps/place/{{ group.location.address | url_encode }}" target="_blank"><img src="/assets/images/icons/icon-location.svg" class="icon icon-location">
                </a>
            </li>
            {% endif %}
        </ul>
    </footer>
</article>
{% endfor %}
</section>

<hr />

<section id="update_the_list" markdown="1">
Are you an existing group organizer or don't see your group here? Send a Pull Request to add your group listing. You can see the template for groups [here]({{ site.github.repository_url }}/tree/master/{{ page.relative_path }}_data/groups).

</section>