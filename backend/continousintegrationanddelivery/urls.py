from django.urls import path
from . import views



urlpatterns = [
  path('views/index', views.index,name="index"),
  path('views/profile',views.profile,name="profile"),
  path('views/register',views.register,name="register"),
  path('views/login',views.login,name="login"),
  path('views/dashboard',views.dashboard,name="dashboard"),


]
