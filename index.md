---
layout: home
---

<!-- begin index.md -->
<table class="sortable">
<tr><th>Company</th><th>Company home page</th><th>California update</th><th>Vermont ID</th></tr>

{% for page in site.pages %}
    <tr><td><a href=".{{ page.url }}">{% if page.company-name %}{{ page.company-name }}{% else %}<strike>{{ page.url }}</strike>{% endif %}</a></td>
    	<td><a target="_blank" href="{{ page.home }}">{{ page.domain }}</a></td>
    	<td>{{ page.california-date }}</td>
    	<td>{% if page.vermont-id %}<a target="_blank" href="https://bizfilings.vermont.gov/online/DatabrokerInquire/DataBrokerInformation?businessID={{ page.vermont-id }}"> {{ page.vermont-id }}</a>{% endif %}</td>
	</tr>
{% endfor %}

</table>
<!-- end index.md -->



