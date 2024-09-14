from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name="new-post"), # has to be above slug 
    path('<slug:slug>', views.post_page, name="page"), #slug path converter 
]
