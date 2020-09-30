from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	path('in/', in_file, name='in'),
	path('out/', out_file, name='out'),
]