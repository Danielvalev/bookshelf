from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.models import UserProfile
from books.models import Book
from accounts.forms import RegisterForm, ProfileForm, LoginForm, UserProfileEditForm


# Create your views here.


# @transaction.atomic
# def register_user(request):
#     if request.method == 'GET':
#         context = {
#             'form': RegisterForm(),
#             'profile_form': ProfileForm(),
#
#         }
#         return render(request, 'accounts/register.html', context)
#     else:  # POST
#         user_form = RegisterForm(request.POST)
#         profile_form = ProfileForm(request.POST, request.FILES)  # request.FILES is mandatory for MEDIA
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             login(request, user)  # login the user
#             return redirect('index')
#
#         context = {
#             'form': RegisterForm(),
#             'profile_form': ProfileForm(),
#         }
#
#         return render(request, 'accounts/register.html', context)


class RegisterView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()

        # Create profile
        profile = UserProfile(user=user)
        profile.save()

        login(self.request, user)
        return valid


# Used in login_user
# def get_redirect_url(params):
#     redirect_url = params.get('return_url')
#     if not redirect_url:
#         return 'index'
#     return redirect_url


# def login_user(request):
#     if request.method == 'GET':
#         login_form = LoginForm()
#
#         context = {
#             'form': login_form,
#         }
#
#         return render(request, 'accounts/login.html', context)
#     else:
#         login_form = LoginForm(request.POST)
#         return_url = get_redirect_url(request.POST)
#
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect(return_url)
#
#         context = {
#             'form': login_form,
#         }
#
#         return render(request, 'accounts/login.html', context)

# Login CBV
class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


# @login_required
# def logout_user(request):
#     logout(request)
#     return redirect('index')


# CBV
class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    books = Book.objects.filter(user=request.user)
    if request.user != user.userprofile.user:
        # Cannot do it
        # raise Exception('You have no permission to do that!')
        return render(request, 'no_permission.html')
    if request.method == 'GET':
        context = {
            'can_edit': request.user == user.userprofile.user,
            'profile_user': user,
            'profile': user.userprofile,
            'books': books,
        }
        return render(request, 'accounts/profile.html', context)


def user_profile_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.user != user.userprofile.user:
        return render(request, 'no_permission.html')

    if request.method == 'GET':
        context = {
            'form_user_profile': UserProfileEditForm(instance=user),
            'form_profile': ProfileForm(instance=user.userprofile),
        }
        return render(request, 'accounts/profile_edit.html', context)
    else:
        form_user = UserProfileEditForm(
            request.POST,
            instance=user
        )
        form_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=user.userprofile
        )
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            return redirect('user profile', user.pk)

        context = {
            'form_user_profile': UserProfileEditForm(instance=user),
            'form_profile': ProfileForm(instance=user.userprofile),
        }
        return render(request, 'accounts/profile_edit.html', context)
