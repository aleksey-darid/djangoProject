from inspect import Traceback
from django.contrib.auth.models import Group, Permission
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def registration_app(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.groups.add(Group.objects.get(name='Users'))
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration_app.html', {'form': form})


def login_app(request):
    """Используется система аутентификации и авторизации django"""
    if request.method == "GET":
        return render(request, "login_page.html")
    elif request.method == "POST":
        message = {"message": "Вы вошли в систему!"}
        error_message = {"error_message": "Не верный логин или пароль, попробуйте снова или зарегестрируйтесь"}
        username = request.POST['username']  # Получаем знычение username
        password = request.POST['password']  # Получаем знычение password
        user = authenticate(username=username, password=password)  # Проверяем есть ли такой пользователь
        if user is not None:
            t = login(request, user)  # Если такой пользователь есть - осуществляем привязку к сессии
            return render(request, "login_page.html", context=message)
        else:
            return render(request, "login_page.html", context=error_message)


def logout_app(request):
    if request.method == "GET":
        return render(request, "logout_page.html")
    elif request.method == "POST":
        logout_message = {"logout_message": "Вы вышли из системы"}
        logout(request)
        return render(request, "logout_page.html", context=logout_message)


def user_app(request):
    if request.method == "GET":
        dat = Group.objects.filter(name='Users').in_bulk()
        print(dat)
        #  dat = User.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        dat_list = list(dat_list1)
        new_dat = []

        count = 0
        for i in dat_list:
            count += 1
            if count == 2:
                new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")
        users_list = {"users_list": new_dat2}
        return render(request, "users_app.html", context=users_list)
    return render(request, "users_app.html")


def workers_app(request):
    if request.method == "GET":
        dat = User.objects.filter(groups__name="Workers")
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        dat_list = list(dat_list1)
        new_dat = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 10:
                new_dat.append(i)
            elif count == 38:
                new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">",
                                                                                           "").replace(")",
                                                                                                       "").replace('"',
                                                                                                                   "")
        workers_list = {"workers_list": new_dat2}
        return render(request, "workers_app.html", context=workers_list)
    return render(request, "workers_app.html")


def administration_app(request):
    return render(request, "administration_app.html")

def home_app(request):
    return render(request, "home_app.html")