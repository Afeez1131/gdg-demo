from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.homepage, name='post_list'),
    path('create-post/', views.create_post, name='create_post'),
    path('update-post/<bid>/', views.update_post, name='update_post'),
    path('post/<slug>/', views.detail_post, name='post_detail'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
