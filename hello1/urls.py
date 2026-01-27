from django.urls import path

from . import views

app_name = "hello1"
urlpatterns = [
    path('', views.myview, name='myview'),   
]