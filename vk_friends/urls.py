from django.conf.urls import url
from django.urls import include, path

from vk_friends.views import index

urlpatterns = [
    path(r'', index),
]