
from django.urls import path
from .views import index, post_request, my_form

urlpatterns = [
    path('', index),
    path('register/',post_request),
    path('register-post/',my_form),
]
