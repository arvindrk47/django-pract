from django.urls import path
from . import views



urlpatterns = [
    path('home/',views.Homeview.as_view()),
    path('authorized', views.Authorizedview.as_view()),
]