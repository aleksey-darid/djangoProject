import datetime
from inspect import Traceback
from django.contrib.auth.models import Group, Permission
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from Management.models import ProductionModel
from Users.forms import OrderForm, UserForm
from Users.models import OrderModel, WorkersModel
from Users.serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


class Workers:

    def workers_get(self, request):
        if request.method == "GET":
            dat = User.objects.filter(groups__name="Workers")
            return render(request, "workers_app.html", {"dat": dat})
        return render(request, "workers_app.html")

    def workers_add(self, request):
        if request.method == "GET":
            dat = User.objects.filter(groups__name="Workers")
            return render(request, "workers_add.html", {"dat": dat})
        elif request.method == "POST" and request.POST.get("add"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            data = request.POST.get
            name = data("name")
            pay = data("pay")
            if name and pay:
                user = User.objects.get(id=name)
                user.groups.add(Group.objects.get(name='Workers'))
                WorkersModel.objects.create(user=user, rate_per_hour=pay)
                return redirect("workers")
            else:
                return render(request, "workers_add.html", context=message_empty)
        return render(request, "workers_app.html")

    def workers_del(self, request):
        if request.method == "GET":
            dat = User.objects.filter(groups__name="Workers")
            return render(request, "workers_del.html", {"dat": dat})
        elif request.method == "POST" and request.POST.get("del"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            data = request.POST.get
            del_name = data("del_name")
            if del_name:
                d = WorkersModel.objects.get(id=del_name)
                d.user.groups.clear()
                d.user.groups.add(Group.objects.get(name='Users'))
                d.delete()
                return redirect("workers")
            else:
                return render(request, "workers_del.html", context=message_empty)
        return render(request, "workers_app.html")

    def workers_put(self, request):
        if request.method == "GET":
            dat = User.objects.filter(groups__name="Workers")
            return render(request, "workers_put.html", {"dat": dat})
        elif request.method == "POST" and request.POST.get("put"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            message_err = {"message_err": "Проверьте правильность вводимой информации!"}
            data = request.POST.get
            id = data("id")
            pay = data("pay")
            if id and pay:
                try:
                    s = WorkersModel.objects.get(id=id)
                    s.rate_per_hour = pay
                    s.save()
                    return redirect("workers")
                except:
                    return render(request, "workers_put.html", context=message_err)
            else:
                return render(request, "workers_put.html", context=message_empty)
        return render(request, "workers_app.html")


def users_app(request):
    if request.method == "GET":
        form = User.objects.all()
        return render(request, "users.html", {"form": form})


def order_app(request):
    if request.method == "GET":
        form = OrderForm(request.GET)
        return render(request, "order_app.html", {"form": form})
    elif request.method == "POST":
        form = OrderForm(request.POST)
        user_id = request.session.get("_auth_user_id")
        user = User.objects.get(id=user_id)
        form.is_valid()
        product = form.cleaned_data.get('product')
        how_math = form.cleaned_data.get('how_math')
        phone = form.cleaned_data.get('phone')
        OrderModel.objects.create(user=user, product=product, how_math=how_math, phone=phone)
        return render(request, "production_app.html", {"message": "Ваш заказ принят в обработку,"
                                                                  " в ближайшее время менеджер свяжется"
                                                                  " с вами для уточнения деталей."})
    return render(request, "order_app.html")


def look_order_app(request):
    if request.method == "GET":
        orders = OrderModel.objects.all()
        return render(request, "look_order.html", {"orders": orders})
    elif request.method == "POST":
        pass


def home_app(request):
    title = {"title": "Главная страница"}
    return render(request, "base.html", context=title)
