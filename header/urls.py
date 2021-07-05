from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sai/', views.message, name='message'),
]
