from django.urls import path
from . import views             

urlpatterns = [
    path('home/', views.index, name='home'),
    path('create/', views.create, name='create'),   
    path('vote/<int:id>/', views.vote, name='vote'),    
    path('result', views.result, name='result'),     
    
]