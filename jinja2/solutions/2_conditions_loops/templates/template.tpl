{% for number in range(10) recursive %}
{% if number % 2 == 0 -%}
interface Gi0/0/0.{{number}}
 no shut
 policy-map {{ name_linkt }}
{% else -%}
interface Gi0/0/0.{{number}}
 no shut
 policy-map {{ name_altitude }}
{% endif -%}
{% endfor %}