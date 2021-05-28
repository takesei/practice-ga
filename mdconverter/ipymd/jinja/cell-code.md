```{{ lang }}
{{ source_batch }}
```

{% if stdout_batch != [] %}
{% for out in stdout_batch %}
:::info STDOUT
```text
{{ out }}
```
:::
{% endfor %}
{% endif %}


{% if stderr_batch != [] %}
{% for err in stderr_batch %}
:::caution STDERR
```text
{{ err }}
```
:::
{% endfor %}
{% endif %}

{% if error != [] %}
{% for e in error %}
:::danger {{ e.ename }}
> {{ e.evalue }}

```text 
{{ e.traceback }}
```
:::
{% endfor %}
{% endif %}


{% if text_plain_batch != [] %}
{% for txt in text_plain_batch %}
:::note Out
```text
{{ txt }}
```
:::
{% endfor %}
{% endif %}


{% if image_png != [] %}
{% for img in image_png %}
:::note Out
![{{ img|safe }}]({{ img|safe }})
:::
{% endfor %}
{% endif %}

{% if text_html != [] %}
{% for html in text_html %}
:::note Out
{{ html }}
:::
{% endfor %}
{% endif %}
