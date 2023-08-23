from django.urls import path
from . import views


urlpatterns=[
    path('register/', views.UserRegistrationview.as_view()),
    path('login/',views.UserLogin.as_view()),
    path('profile/', views.ProfileView.as_view()),
    ]