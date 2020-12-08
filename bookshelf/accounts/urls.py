from django.urls import path

from accounts.views import login_user, logout_user, register_user, user_profile

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', register_user, name='register user'),
    # path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>', user_profile, name='user profile'),

]
