```{{ lang }}
{{ source_batch }}
```

{% if output|length > 0 -%}
<Tabs
defaultValue='{{ first_element }}'
values={[
{% for k, v in output.items() -%}
{% if v != [] -%}
{% if k == "stdout_batch" -%}
{label: "STDOUT", value: '{{ k }}'},
{% elif k == "stderr_batch" -%}
{label: "STDERR", value: '{{ k }}'},
{% elif k == "error" -%}
{label: "ERROR", value: '{{ k }}'},
{% elif k == "text_plain_batch" -%}
{label: "[Out]", value: '{{ k }}'},
{% elif k == "image_png" -%}
{label: "Image", value: '{{ k }}'},
{% elif k == "text_html" -%}
{label: "HTML", value: '{{ k }}'},
{% endif -%}
{% endif -%}
{% endfor -%}
]}>

{% for k, v in output.items() -%}
{% if v != [] -%}
<TabItem value='{{ k }}'>
{% if k == "stdout_batch" -%}
{% for cont in v %}
:::info STDOUT
```text
{{ cont }}
```
:::
{% endfor -%}
{% elif k == "stderr_batch" -%}
{% for cont in v %}
:::caution STDERR
```text
{{ cont }}
```
:::
{% endfor -%}
{% elif k == "error" -%}
{% for cont in v %}
:::danger {{ cont.ename }}
```text 
{{ cont.traceback }}
```
:::
{% endfor -%}
{% elif k == "text_plain_batch" -%}
{% for cont in v %}
:::note Out
```text
{{ cont }}
```
:::
{% endfor -%}
{% elif k == "image_png" -%}
{% for cont in v %}
:::note Image
![{{ cont|safe }}]({{ cont|safe }})
:::
{% endfor -%}
{% elif k == "text_html" -%}
{% for cont in v %}
:::note HTML
{{ cont }}
:::
{% endfor -%}
{% endif -%}
</TabItem>
{% endif -%}
{% endfor -%}
</Tabs>
{% endif %}

---
