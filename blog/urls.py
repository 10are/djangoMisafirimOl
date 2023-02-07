from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('createblog/',views.createblog, name="create_blog"),
    path('myblog/',views.myblog, name="my_blog")
]