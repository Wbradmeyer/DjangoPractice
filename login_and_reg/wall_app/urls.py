from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_wall), 
    path('messages', views.create_message),
    path('comments', views.create_comment),
    path('messages/delete/<int:message_id>', views.delete_message)
]