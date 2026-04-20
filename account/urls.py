from django.urls import path
from . import views

urlpatterns = [
    path('register/',  views.register,      name='register'),
    path('login/',     views.login,          name='login'),
    path('logout/',    views.logout_clear,   name='logout'),
    path('checkform/', views.checkformview,  name='checkform'),
]
