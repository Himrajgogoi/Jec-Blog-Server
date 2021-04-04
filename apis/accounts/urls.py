from rest_framework import routers
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, Profile, PersonalUser
from knox import views as knox_views

router = routers.DefaultRouter()
router.register("api/user/profile", Profile, "profile")
router.register("api/users", UserAPI, "users")

urlpatterns = [
    path("api/auth", include('knox.urls')),
    path("api/auth/register", RegisterAPI.as_view()),
    path("api/auth/login", LoginAPI.as_view()),
    path("api/auth/user", PersonalUser.as_view()),
    path("api/auth/logout", knox_views.LogoutView.as_view(), name = "knox_logout"),
    path('', include(router.urls)),
]
