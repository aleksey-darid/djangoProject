import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from Administration.models import ScheduleModel, BidModel
from Users.models import WorkersModel, OrderModel
from .models import SuppliersModel, ProductionModel, SupplyModel, WagesModel
from .serializers import SupplySerializer, SuppliersSerializer, ProductionSerializer, WagesSerializer


class SupplyView(ModelViewSet):
    queryset = SupplyModel.objects.all()
    serializer_class = SupplySerializer


def Sup_app(request):
    return render(request, "suppliers_api_app.html")


class SuppliersView(ModelViewSet):
    queryset = SuppliersModel.objects.all()
    serializer_class = SuppliersSerializer


class ProductionView(ModelViewSet):
    queryset = ProductionModel.objects.all()
    serializer_class = ProductionSerializer


class WagesView(ModelViewSet):
    queryset = WagesModel.objects.all()
    serializer_class = WagesSerializer


class Supply:

    def supply_get(self, request):
        if request.method == "GET":
            dat = SupplyModel.objects.all()
            return render(request, "supply_app.html", {'dat': dat, 'title': "Поставки"})
        return render(request, "supply_app.html")

    def supply_add(self, request):
        if request.method == "GET":
            dat = SupplyModel.objects.all()
            dat2 = SuppliersModel.objects.all()
            return render(request, "supply_add.html", {'dat': dat, "dat2": dat2, "title": "Поставки"})
        elif request.method == "POST" and request.POST.get("add"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            message_err = {"message_err": "Проверьте правильность вводимой информации!"}
            data = request.POST.get
            sup = data("sup")
            dat = data("dat")
            amo = data("amo")
            if sup and dat and amo:
                try:
                    supplier = SuppliersModel.objects.get(id=sup)
                    SupplyModel.objects.create(supplier=supplier, date=dat, amount=amo)
                    return redirect("supply_get")
                except:
                    return render(request, "supply_add.html", context=message_err)
            else:
                return render(request, "supply_add.html", context=message_empty)
        return render(request, "supply_app.html")

    def supply_del(self, request):
        if request.method == "GET":
            dat = SupplyModel.objects.all()
            return render(request, "supply_del.html", {'dat': dat, 'title': "Поставки"})
        elif request.method == "POST" and request.POST.get("del"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            data = request.POST.get
            del_id = data("del_id")
            if del_id:
                d = SupplyModel.objects.filter(id=del_id)
                d.delete()
                return redirect("supply_get")
            else:
                return render(request, "supply_del.html", context=message_empty)
        return render(request, "supply_app.html")

    def supply_put(self, request):
        if request.method == "GET":
            dat = SupplyModel.objects.all()
            return render(request, "supply_put.html", {'dat': dat, 'title': "Поставки"})
        elif request.method == "POST" and request.POST.get("put"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            message_err = {"message_err": "Проверьте правильность вводимой информации!"}
            data = request.POST.get
            put_id = data("put_id")
            suplier = data("sup")
            date = data("dat")
            amo = data("amo")
            if put_id and suplier and date and amo:
                try:
                    supply = SupplyModel.objects.get(id=f"{put_id}")
                    supplier = SuppliersModel.objects.get(name=supply.supplier.name)
                    supply.supplier = supplier
                    supply.date = date
                    supply.amount = amo
                    supply.save()
                    return redirect("supply_get")
                except:
                    return render(request, "supply_put.html", context=message_err)
            else:
                return render(request, "supply_put.html", context=message_empty)
        return render(request, "supply_app.html")


class Suppliers:

    def suppliers_get(self, request):
        if request.method == "GET":
            dat = SuppliersModel.objects.all()
            return render(request, "suppliers_app_.html", {"dat": dat})
        return render(request, "suppliers_app_.html")

    def suppliers_add(self, request):
        if request.method == "GET":
            dat = SuppliersModel.objects.all()
            return render(request, "suppliers_add.html", {"dat": dat})
        elif request.method == "POST" and request.POST.get("add"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            data = request.POST.get
            name = data("name")
            pay_def = data("pay_def")
            if name and pay_def:
                SuppliersModel.objects.create(name=f"{name}", payment_deferment=f"{pay_def}")
                return redirect("suppliers_get")
            else:
                return render(request, "suppliers_add.html", context=message_empty)
        return render(request, "suppliers_app_.html")

    def suppliers_del(self, request):
        if request.method == "GET":
            dat = SuppliersModel.objects.all()
            return render(request, "suppliers_del.html", {"dat": dat})
        elif request.method == "POST" and request.POST.get("del"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            data = request.POST.get
            del_name = data("del_name")
            if del_name:
                d = SuppliersModel.objects.filter(id=del_name)
                d.delete()
                return redirect("suppliers_get")
            else:
                return render(request, "suppliers_del.html", context=message_empty)
        return render(request, "suppliers_app_.html")

    def suppliers_put(self, request):
        if request.method == "GET":
            dat = SuppliersModel.objects.all()
            return render(request, "suppliers_put.html", {"dat": dat})
        elif request.method == "POST" and request.POST.get("put"):
            message_empty = {"message_empty": "Поля не могут быть пустыми!"}
            message_err = {"message_err": "Проверьте правильность вводимой информации!"}
            data = request.POST.get
            put_name = data("put_name")
            name = data("name")
            pay_def = data("pay_def_put")
            if put_name and name and pay_def:
                try:
                    s = SuppliersModel.objects.get(id=f"{put_name}")
                    s.name = f"{name}"
                    s.payment_deferment = f"{pay_def}"
                    s.save()
                    return redirect("suppliers_get")
                except:
                    return render(request, "suppliers_put.html", context=message_err)
            else:
                return render(request, "suppliers_put.html", context=message_empty)
        return render(request, "suppliers_app_.html")


def production_app(request):
    if request.method == "GET":
        product = ProductionModel.objects.all()
        return render(request, "production_app.html", {"product": product})
    return render(request, "production_app.html")


def wages_app(request):
    if request.method == "GET":
        worker = WorkersModel.objects.all()
        return render(request, "wages_app.html", {"worker": worker})
    elif request.method == "POST":
        data = request.POST.get
        id_worker = data("worker")
        try:
            u_worker = WorkersModel.objects.get(pk=id_worker)
            worker = User.objects.get(workersmodel=u_worker)
            date_from = datetime.datetime.strptime(data("from"), "%Y-%m-%d")
            date_to = datetime.datetime.strptime(data("to"), "%Y-%m-%d")
            days_list = list()
            work_days = ScheduleModel.objects.filter(worker=worker)
            for i in work_days:
                if datetime.datetime.combine(i.date, datetime.time()) >= date_from and datetime.datetime.combine(i.date,
                                                                                                                 datetime.time()) <= date_to:
                    days_list.append(i)
            delta_list = list()
            for i in days_list:
                delta_list.append(i.delta)
            s = 0
            for i in delta_list:
                s += i
            hours = s / 60
            r_p_h = int(u_worker.rate_per_hour)
            pay = hours * r_p_h
            pay1 = {"pay": pay, "pay_text": "Ваша ЗП за выбраный период составит -", "r": "р."}
            sch1 = WagesModel(worker=worker, date_from=date_from, date_to=date_to, hours=hours, total_wages=pay)
            sch1.save()
            return render(request, "wages_app.html", context=pay1)
        except:
            return render(request, "wages_app.html", {"message2": "Неверный ID"})

    return redirect("wages")


def look_order_app(request):
    if request.method == "GET":
        orders = OrderModel.objects.all()
        return render(request, "look_order.html", {"orders": orders})
    elif request.method == "POST":
        pass


def look_bid_app(request):
    if request.method == "GET":
        bid = BidModel.objects.all()
        return render(request, "look_bid.html", {"bid": bid})
    elif request.method == "POST":
        pass



