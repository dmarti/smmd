---
layout: home
---

<!-- begin index.md -->

<!-- List broken domains -->
{% for page in site.pages %}
	{% if page.url contains "domain" %}
		{% unless page.company-name or page.owned-by %}
<div><form method="GET" action="https://github.com/dmarti/smmd/blob/gh-pages/{{ page.url }}/index.md">
<span class="broken">Broken listing:</span>&nbsp;<a href=".{{ page.url }}">{{ page.url }}</a>&nbsp;<input type="submit" value="Fix it"></form></div><br>
		{% endunless %}
	{% endif %}
{% endfor %}

<table class="sortable">
<tr><th>Company</th><th>Company home page</th><th>California update</th><th>Vermont ID</th></tr>

<!-- Only list domains with meaningful data (broken entries go at the top) -->
{% for page in site.pages %}
	{% if page.company-name or page.powned-by %}
    <tr><td><a href=".{{ page.url }}">{% if page.company-name %}{{ page.company-name }}{% else %}<strike>{{ page.url }}</strike>{% endif %}</a></td>
    	<td><a target="_blank" href="{{ page.home }}">{{ page.domain }}</a></td>
    	<td>{{ page.california-date }}</td>
    	<td>{% if page.vermont-id %}<a target="_blank" href="https://bizfilings.vermont.gov/online/DatabrokerInquire/DataBrokerInformation?businessID={{ page.vermont-id }}"> {{ page.vermont-id }}</a>{% endif %}</td>
	</tr>
	{% endif %}
{% endfor %}

</table>
<!-- end index.md -->



