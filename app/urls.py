from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('read/<int:uid>/',views.read,name='read'),
]