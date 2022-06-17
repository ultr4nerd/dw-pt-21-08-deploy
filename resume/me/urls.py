"""Me app URL config"""

from django.urls import path

from . import views

app_name = "me"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<str:username>", views.ProfileView.as_view(), name="profile"),
]
