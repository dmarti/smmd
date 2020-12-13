---
section: list
layout: index
title: High priority domains
list: high-priority
---

<h1>{{ page.path }} </h1>

<table class="sortable">
<tr><th>List name</th><th colspan="2">Domain</th></tr>
{% for p in site.list %}
	{% if p.domain and p.list == page.list %}
	<tr id="{{ p.list }}-{{ p.domain }}" >
		<td><a href="/list/{{ p.list }}">{% if p.list-name %}
	 		{{ p.list-name }}
		{% else %}
			{{ p.list }}
		{% endif %}</a></td>
		<td><a href="../domain/{{p.domain}}/">{{ p.domain }}</a></td><td>
<a href="https://github.com/dmarti/smmd/blob/gh-pages/_list/{{ p.list }}/{{ p.domain}}/index.md">(edit listing)</a></td></tr>
	{% endif %}
{% endfor %}
</table>

