from django.urls import path
from seapp import views

urlpatterns = [
    path('', views.index,name='index'),
]
