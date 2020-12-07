from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, ProfileForm, LoginForm


# Create your views here.


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),

        }
        return render(request, 'accounts/register.html', context)
    else:  # POST
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)  # request.FILES is mandatory for MEDIA

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # login the user
            return redirect('index')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'accounts/register.html', context)


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    if not redirect_url:
        return 'index'
    return redirect_url


def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        return_url = get_redirect_url(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(return_url)

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.user != user.userprofile.user:
        # Cannot do it
        raise Exception('You have no permission to do that!')
    if request.method == 'GET':
        context = {
            'can_edit': request.user == user.userprofile.user,
            'profile_user': user,
            'profile': user.userprofile,
        }
        return render(request, 'accounts/profile.html', context)
    else:
        pass
