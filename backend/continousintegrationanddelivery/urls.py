from django.urls import path
from . import views



urlpatterns = [
  path('', views.index,name="index"),
  path('profile',views.profile_management,name="profile"),
  path('register',views.register,name="register"),
  path('login',views.login,name="login"),
  path('dashboard',views.dashboard,name="dashboard"),
path('logout',views.user_logout,name="logout"),
path('delete',views.delete_Account,name="delete"),

]
