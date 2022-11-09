from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='post_list'),
    path('create-post/', views.create_post, name='create_post'),
]
