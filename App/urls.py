from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.saveContactus, name='contact'),
    path('register/', views.register, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('profile/', views.profile, name='profile'),
    path('registerCustomer/', views.registerCustomer, name='registerCustomer'),
    path('attendance/<str:id>', views.attendance, name='attendance'),
    path('customers/<str:id>', views.customers, name='customers'),
    path('requestedCustomer/<str:id>', views.requestedCustomer, name='requestedCustomer'),
    path('logoutUser/', views.logoutuser, name='logoutUser'),
    path('requestedProfile/<str:id>', views.requestedProfile, name='requestProfile'),
]
