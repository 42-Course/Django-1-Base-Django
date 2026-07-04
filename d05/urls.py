from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home),
    path('', include('ex00.urls')),
    path('', include('ex01.urls')),
    path('', include('ex02.urls')),
    path('', include('ex03.urls')),
]
