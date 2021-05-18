from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.HellowApiView.as_view()),
]
