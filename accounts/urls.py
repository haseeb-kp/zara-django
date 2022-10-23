from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name="index"),
    path('user_login', views.user_login, name="user_login"),
    path('user_signup', views.user_signup, name="user_signup"),
    path('home', views.home, name="home"),
    path('products/<int:id>/', views.products, name="products"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('number_check', views.number_check, name="number_check"),
    path('otp_validate', views.otp_validate, name="otp_validate"),
    path('signup_otp_validate', views.signup_otp_validate, name="signup_otp_validate"),

    
]