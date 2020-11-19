from django.urls import path
from django.urls.conf import include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user-viewset', views.UserViewSet, basename="user-viewset")

urlpatterns = [
    path('hello/', views.User.as_view()),
    path('', include(router.urls))
]

