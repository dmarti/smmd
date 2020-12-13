---
section: list
layout: index
title: Domains on lists
---

<table class="sortable">
<tr><th>List name</th><th colspan="2">Domain</th></tr>

{% for page in site.list %}
	{% if page.domain %}
	<tr id="{{ page.list }}-{{ page.domain }}" >
		<td><a href="/list/{{ page.list }}">{% if page.list-name %}
	 		{{ page.list-name }}
		{% else %}
			{{ page.list }}
		{% endif %}</a></td>
		<td><a href="../domain/{{page.domain}}/">{{ page.domain }}</a></td><td>
<a href="https://github.com/dmarti/smmd/blob/gh-pages/_list/{{ page.list }}/{{ page.domain}}/index.md">(edit listing)</a></td></tr>
	{% endif %}
{% endfor %}

</table>



