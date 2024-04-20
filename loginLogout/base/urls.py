from django.urls import path, include
from .views import profile
from .views import profile, logoutaccount

urlpatterns = [

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", profile, name="profile"),
    path("accounts/logoutaccount/", logoutaccount, name="logout"),

]
