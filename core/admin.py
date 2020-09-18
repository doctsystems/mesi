from django.contrib import admin
from .models import *

class SingletonModelAdmin(admin.ModelAdmin):
	exclude = ['estado']
	actions = None  

	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request):
		return False

@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
	pass

# admin.site.register(SiteSettings)
