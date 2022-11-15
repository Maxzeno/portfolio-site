from django import template


register = template.Library()


@register.filter
def start_dash_end(value):
	""" return start - end """
	if value.start:
		return f"{value.start} - {value.end if value.end else 'Present'}"
	return value.end if value.end else ''

