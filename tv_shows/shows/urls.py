from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    path('', views.index),
    path('shows', views.dashboard, name='dashboard'),
    path('shows/create', views.create_show, name='create_show'),
    path('shows/new', views.new_show, name='new_show'),
    path('shows/<int:show_id>', views.one_show, name='one_show'),
    path('shows/<int:show_id>/edit', views.edit_show, name='edit'),
    path('shows/<int:show_id>/update', views.update_show, name='update'),
    path('shows/<int:show_id>/destroy', views.delete_show, name='delete')
]