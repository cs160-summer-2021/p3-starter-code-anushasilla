from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('landing', views.landing, name='landing'),
    path('triangle', views.triangle, name='triangle'),
    path('flowers', views.flowers, name='flowers'),
    path('blank', views.blank, name='blank')
        
]
