from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saved_blog', views.saved_blog, name='saved_blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.user_profile, name='profile'),
    path('generate-blog', views.generate_blog, name='generate- blog '),
]