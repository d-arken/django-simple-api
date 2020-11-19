from django.urls import path
from api.views import User
urlpatterns = [
    path('hello/', User.as_view())
]
