{% extends "parent_template_block.tpl" %}

{% block interface %}
interface Gi0/0/0.{{number}}
 no shut
 policy-map {{ name }}
{% endblock %}