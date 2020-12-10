from django.urls import path

from accounts.views import user_profile, LogoutView, LoginView, RegisterView

urlpatterns = [
    # path('login/', login_user, name='login user'),
    path('login/', LoginView.as_view(), name='login user'),  # CBV
    # path('logout/', logout_user, name='logout user'),
    path('logout/', LogoutView.as_view(), name='logout user'),  # CBV
    # path('register/', register_user, name='register user'),
    path('register/', RegisterView.as_view(), name='register user'), # CBV
    # path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>', user_profile, name='user profile'),

]
