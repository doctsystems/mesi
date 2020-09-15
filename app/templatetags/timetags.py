from django import template
import datetime
register = template.Library()

def timestamp_to_date(timestamp):
	# print('*********** timestamp: ', timestamp, ' **********************')
	try:
		ts = int(timestamp)
		# print('------- ts: ', ts, ' --------')
	except ValueError:
		return 0
	# print('********* ', datetime.date.fromtimestamp(ts), '************')
	return datetime.date.fromtimestamp(ts)

register.filter(timestamp_to_date)

@register.filter('timestamp_to_time')
def convert_timestamp_to_time(timestamp):
    import time
    return datetime.date.fromtimestamp(int(timestamp))