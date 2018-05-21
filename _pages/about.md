---
layout: single
title: About
permalink: /about/
---
KnoxDevs is a registered non-profit organization whose sole mission is to foster a healthy software developer community in Knoxville, TN.

## Board
<section class="cards">
{% assign board = site.board | sort: 'rank' %}
{% for member in board %}
<article class="card">
    <header class="card__title">
      <h3>{{member.name}}</h3>
      <h5>{{member.position}}</h5>
    </header>
    <figure class="card__image">
        <img src="{{member.image}}">
    </figure>
    <main class="card__description">
      {{ member.content | strip_html | truncatewords:50 }}
    </main>
  <footer class="card__footer">
      <ul>
          {% if member.online.github %}
          <li><a href="https://github.com/{{ member.online.github }}" target="_blank"><img src="/assets/images/icon-github.svg" class="icon icon-github"></a></li>
          {% endif %}
          {% if member.online.twitter %}
          <li><a href="https://twitter.com/{{ member.online.twitter }}" target="_blank"><img src="/assets/images/icon-twitter.svg" class="icon icon-twitter"></a></li>
          {% endif %}
          {% if member.online.website %}
          <li><a href="http://{{ member.online.website }}" target="_blank"><img src="/assets/images/icon-link.svg" class="icon icon-website"></a></li>
          {% endif %}
      </ul>
  </footer>
</article>
{% endfor %}
</section>

## Code of Conduct

### Our Pledge
KnoxDevs is dedicated to providing an outstanding experience, to increase learning opportunities for all our members, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

We do not tolerate harassment of members in any form, and we would like to take this opportunity to remind all members that KnoxDevs was founded on: passionate, but respectful dialog between our members, for our members. Please treat your fellow members with respect!

Harassment<sup>[1](#fn1)</sup> is not appropriate for any group venue. Group members violating these rules may be sanctioned or expelled from the group, at the discretion of the group organizers.

Members must remember that KnoxDevs organizers and volunteers are not trained conflict resolution specialists, nor are they security or law enforcement. KnoxDevs organizers and volunteers will immediately escalate issues around safety, violence, or similar situations to the Knoxville Police Department.

For the protection of both members and our organization, KnoxDevs will never put its organizers or volunteers in the position of trying to assess whether or not an incident merits reporting. If there is any doubt, we will report incidents to the Knoxville Police Department immediately.

### Incident Resolution
Members should follow the golden rule: “One should treat others as one would like others to treat oneself.” Treat other members with respect.
Simple disagreements should be resolved between the individuals concerned.
Harassment or more serious issues should be escalated to a KnoxDevs organizer. That organizer will immediately contact a KnoxDevs Board member who has the responsibility to assist in resolution.

><a name="fn1">1</a>: Examples include offensive comments, verbal threats or demands, sexualized images in public spaces, intimidation, stalking, harassing photography or recording, sustained disruption of sessions or events, unwelcome physical contact or sexual attention, and the advocating or encouragement of any of the above behavior.
