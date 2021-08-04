from django.urls import include, path, re_path

from app import urls

urlpatterns = [
    path('', include(urls)),
    # re_path(r'^', include(urls)),
]
