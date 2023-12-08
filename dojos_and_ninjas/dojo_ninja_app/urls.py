from django.urls import path
from . import views

app_name = 'create'

urlpatterns = [
    path('', views.index),
    path('dojos/new', views.create_dojo, name='dojo'),
    path('ninjas/new', views.create_ninja, name='ninja'),
    path('dojos/<int:dojo_id>/delete', views.delete_dojo, name='delete')
]