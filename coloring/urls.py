from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('landing', views.landing, name='landing')
    
]
