from django.urls import path, include

from main.views import auth

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)

]
