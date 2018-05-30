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
      <h3 id="{{group.name | url_encode }}">{{group.name}}</h3>
    </header>
    <figure class="card__image">
        <img src="{{group.image}}">
    </figure>
    <main class="card__description">
        {{ group.blurb | markdownify | truncatewords:50 }}
    </main> 
    <footer class="card__footer">
        {% if group.slack_channel %}
        <img src="/assets/images/icon-slack.svg" class="icon icon-slack">
        <code>
            <a href="https://knoxdevs.slack.com/messages/{{ group.slack_channel }}"  target="_blank" title="Join the conversation on the KnoxDevs slack in the {{ group.slack_channel }} channel!">#{{ group.slack_channel }}</a>
        </code>
        {% endif %}
        <ul>
            {% if group.online.github %}
            <li>
                <a href="https://github.com/{{ group.online.github }}" target="_blank"><img src="/assets/images/icon-github.svg" class="icon icon-github"></a>
            </li>
            {% endif %}
            {% if group.online.meetup %}
            <li>
                <a href="https://meetup.com/{{ group.online.meetup }}" target="_blank">
                    <img src="/assets/images/icon-meetup.svg" class="icon icon-meetup">
                </a>
            </li>
            {% endif %}
            {% if group.online.twitter %}
            <li>
                <a href="https://twitter.com/{{ group.online.twitter }}" target="_blank">
                    <img src="/assets/images/icon-twitter.svg" class="icon icon-twitter">
                </a>
            </li>
            {% endif %}
            {% if group.online.website %}
            <li>
                <a href="{{ group.online.website }}" target="_blank">
                <img src="/assets/images/icon-link.svg" class="icon icon-website">
                </a>
            </li>
            {% endif %}
            {% if group.location.gmap %}
            <li data-toggle="tooltip" data-placement="bottom" title="{{group.location.name}}">
                <a href="https://goo.gl/maps/{{ group.location.gmap }}" target="_blank"><img src="/assets/images/icon-location.svg" class="icon icon-location">
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
Are you an existing group organizer? You can update the listing here by sending a Pull Request to the individual markdown file [here](#).

Do you not see your group here? Send a Pull Request to add your group listing. You can see the template for groups [here](#).

</section>