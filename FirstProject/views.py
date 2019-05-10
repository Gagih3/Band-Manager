from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .form import SignUpForm, LoginForm, ProfileForm
from django.contrib.auth.models import User

class Main (View):

    def get(self, request):

        return render(request, "index.html",)


class SignUp (View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('main')
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/main')


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/main')
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})


class ProfileView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, 'profile.html', context={'form': form})

    def post(self, request):
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data['profile_image'])
            return render(request, 'profile.html')
