from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name = 'homePage'),
    path("project/post/", views.post, name = "post"),
]