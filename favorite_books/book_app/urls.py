from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('new', views.create_book),
    path('<int:book_id>', views.display_book),
    path('<int:book_id>/update', views.update_book),
    path('<int:book_id>/delete', views.delete_book),
    path('<int:book_id>/like', views.like_book),
    path('<int:book_id>/unlike', views.unlike_book),
]