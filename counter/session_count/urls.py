from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('add_two', views.add_two_to_count),
    path('add_custom', views.add_custom_to_count)
]