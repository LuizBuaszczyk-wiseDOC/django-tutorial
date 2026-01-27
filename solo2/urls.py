from django.urls import path

from . import views

app_name = "solo2"
urlpatterns = [
    path("", views.Solo2View.as_view(), name="Solo2View"),
]