from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	path('', HomePageView, name='home'),
	path('institucional/', InstitucionalPageView, name='institucional'),
	path('contacto/', Contacto, name='contacto'),
	path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'), name='logout'),
]