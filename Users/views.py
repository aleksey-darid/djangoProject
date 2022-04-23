from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from Management.models import ProductionModel
from Users.forms import OrderForm
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
            login(request, user)  # Если такой пользователь есть - осуществляем привязку к сессии
            return render(request, "login_page.html", context=message)
        else:
            return render(request, "login_page.html", context=error_message)


def logout_app(request):
    if request.method == "GET":
        return render(request, "logout_page.html")
    elif request.method == "POST":
        logout(request)
        return redirect("home")


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
    message = {"message": "Ваш заказ принят в обработку, в ближайшее время менеджер свяжется с вами для уточнения "
                          "деталей."}
    if request.method == "GET":
        form = OrderForm(request.GET)
        return render(request, "order_app.html", {"form": form})
    elif request.method == "POST":
        form = OrderForm(request.POST)
        user_id = request.session.get("_auth_user_id")
        form.is_valid()
        product = form.cleaned_data.get('product')
        how_math = form.cleaned_data.get('how_math')
        phone = form.cleaned_data.get('phone')
        if user_id:
            user = User.objects.get(id=user_id)
            OrderModel.objects.create(user=user, product=product, how_math=how_math, phone=phone)
            return render(request, "production_app.html", context=message)
        else:
            OrderModel.objects.create(product=product, how_math=how_math, phone=phone)
            return render(request, "production_app.html", context=message)
    return render(request, "order_app.html")


def home_app(request):
    data = {"title": "AMENIEL COFFEE"}
    if request.method == "GET":
        user_id = request.session.get("_auth_user_id")
        try:
            user = User.objects.get(id=user_id)
            groups = user.groups.filter()
            group1 = groups[0].name
            try:
                group2 = groups[1].name
                if group1 == "Users" and group2 == "Workers":
                    return render(request, "base_worker.html", context=data)
                elif group1 == "Users" and group2 == "Manager":
                    return render(request, "base_manager.html", context=data)
                elif group1 == "Users" and group2 == "Dev":
                    return render(request, "base.html", context=data)
                else:
                    return render(request, "base_user.html", context=data)
            except:
                if group1 == "Users":
                    return render(request, "base_user.html", context=data)
                elif group1 == "Workers":
                    return render(request, "base_worker.html", context=data)
                elif group1 == "Manager":
                    return render(request, "base_manager.html", context=data)
                elif group1 == "Dev":
                    return render(request, "base.html", context=data)
                else:
                    return render(request, "base_user.html", context=data)
        except:
            return render(request, "base_user.html")


class First:

    def add_all_first_data(self, request):
        try:
            Group.objects.create(name='Dev')
            Group.objects.create(name='Workers')
            Group.objects.create(name='Users')
            Group.objects.create(name='Manager')
            ses_user = request.user.username
            user = User.objects.get(username=ses_user)
            user.groups.add(Group.objects.get(name='Dev'))
            User.objects.create(username="Manager", password="manager1Manager1")
            User.objects.create(username="User", password="user1User1")
            User.objects.create(username="Worker1", password="worker1Worker1")
            User.objects.create(username="Worker2", password="worker2Worker2")
            # user = authenticate(username=manager.username, password=manager.password)
            user1 = User.objects.get(username="Manager")
            user1.groups.add(Group.objects.get(name='Manager'))
            ProductionModel.objects.create(name="AMENIEL", size="250 g,", price=30)
            ProductionModel.objects.create(name="AMENIEL", size="500 g,", price=50)
            return redirect("home")
        except:
            return render(request, "base_user.html", {"m": "О-ОУ.. Придется в ручную"})
