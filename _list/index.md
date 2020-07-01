---
section: list
layout: section-index
title: Domains on lists
---

<table class="sortable">
<tr><th>List name</th><th>Domain</th></tr>

{% for page in site.list %}	
	<tr><td>{{ page.list-name }}</td><td><a href="../domain/{{page.domain}}/">{{ page.domain }}</a></td></tr>
{% endfor %}

</table>



