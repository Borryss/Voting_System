from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_poll, name='create_poll'),
    path('<uuid:poll_id>/', views.poll_detail, name='poll_detail'),
]