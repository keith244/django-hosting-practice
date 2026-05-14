from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('post_read/<int:post_id>/', views.post_read, name='post_read'),
    path('delete_post/<int:post_id>/', views.post_delete, name='delete_post'),
]