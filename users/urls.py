from django.urls import path
from . import views             

urlpatterns = [
    
    path('', views.signin, name='login'),  
    path('signup/', views.signup, name='signup'),  
    path('signout/', views.signout, name='signout'),           
    
]