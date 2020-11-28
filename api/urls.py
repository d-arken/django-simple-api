from django.urls import path
from django.urls.conf import include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user-viewset', views.UserViewSet, basename="user-viewset")
router.register('profile', views.UserProfileViewSet, basename='profile')

urlpatterns = [
    path('hello/', views.User.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view())
]

