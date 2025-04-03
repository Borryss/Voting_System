from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_poll, name='create_poll'),
    path('<uuid:poll_id>/', views.poll_detail, name='poll_detail'),
    path('ajax_test/', views.ajax_test, name='ajax_test'),  # У цьому випадку цей шлях правильний
]
