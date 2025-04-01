from django.urls import path
from .views import RegisterView, LoginView
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('register/', RegisterView.as_view(), name='register_api'),
    path('login/', LoginView.as_view(), name='login_api'),
    path('login/', views.login_page, name='login_page'),
]