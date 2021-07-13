from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='login'),
    path('userprofile/', views.userprofile, name='user'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('usereditprofile/', views.edit_profile, name='edit_profile'),
    # path('updateuser/<int:profile_id>/', views.user_update_form),

]