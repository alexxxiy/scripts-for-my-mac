{% sql 'insert', note='add text from and to into table' %}
	INSERT INTO {{table}} VALUES ('{{fromText}}','{{toText}}')
{% endsql %}

{% sql 'update', note='update text' %}
	UPDATE {{table}}
	   SET _to = '{{toText}}'
	 WHERE 1=1
	   AND _from = '{{fromText}}'
{% endsql %}

{% sql 'check', note='select' %}
	SELECT _to FROM {{table}} WHERE _from = '{{fromText}}'
{% endsql %}