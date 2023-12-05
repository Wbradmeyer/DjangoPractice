from django.urls import path
from . import views

app_name = 'guesses'

urlpatterns = [
    path('', views.index),
    path('guess_number', views.guess_number, name='guess'),
    path('destroy', views.destroy_session, name='destroy')
]