import datetime

from django.http import request
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Administration.models import ScheduleModel
from .forms import SupplyForm, SuppliersForm, ProductionForm, WagesForm
from .models import SuppliersModel, ProductionModel, SupplyModel, WagesModel
from .serializers import SupplySerializer, SuppliersSerializer, ProductionSerializer, WagesSerializer


class SupplyView(ModelViewSet):
    queryset = SupplyModel.objects.all()
    serializer_class = SupplySerializer


def Sup_app(request):
    return render(request, "suppliers_app.html")


class SuppliersView(ModelViewSet):
    queryset = SuppliersModel.objects.all()
    serializer_class = SuppliersSerializer


class ProductionView(ModelViewSet):
    queryset = ProductionModel.objects.all()
    serializer_class = ProductionSerializer


class WagesView(ModelViewSet):
    queryset = WagesModel.objects.all()
    serializer_class = WagesSerializer


def supply_app(request):
    if request.method == "GET":
        data = SupplyModel.objects.in_bulk()
        dat_list1 = str(data.values()).replace(":", ",").split(",")
        dat_list = list(dat_list1)
        new_dat_sup = []
        new_dat_dat = []
        new_dat_amo = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 4:
                new_dat_sup.append(i)
            elif count == 6:
                new_dat_dat.append(i)
            elif count == 7:
                new_dat_amo.append(i)
                count = 0
        new_dat_sup1 = str(new_dat_sup).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")",
                                                                                                                    "")
        new_dat_dat1 = str(new_dat_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")",
                                                                                                                    "")
        new_dat_amo1 = str(new_dat_amo).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")",
                                                                                                                    "")
        supply_list = {"supply_sup": new_dat_sup1, "supply_dat": new_dat_dat1, "supply_amo": new_dat_amo1}
        return render(request, "supply_app.html", context=supply_list)
    elif request.method == "POST" and request.POST.get("add"):
        message_empty = {"message_empty": "Поля не могут быть пустыми!"}
        data = request.POST.get
        sup = data("sup")
        dat = data("dat")
        amo = data("amo")
        if sup and dat and amo:
            SupplyModel.objects.create(supplier=sup, date=dat, amount=amo) # найти как выбрать поставщика
            return redirect("supply")
        else:
            return render(request, "supply_app.html", context=message_empty)
    elif request.method == "POST" and request.POST.get("del"):
        pass
        return redirect("supply")
    elif request.method == "POST" and request.POST.get("put"):
        pass
        return redirect("supply")


def suppliers_app(request):
    if request.method == "GET":
        dat = SuppliersModel.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        dat_list = list(dat_list1)
        new_dat_name = []
        new_dat_pay = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 3:
                new_dat_name.append(i)
            elif count == 4:
                new_dat_pay.append(i)
                count = 0
        new_dat_name = str(new_dat_name).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(
            ")",
            "")
        new_dat_pay = str(new_dat_pay).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")",
                                                                                                                   "")
        data_h = {"sup": str(new_dat_name), "pay": str(new_dat_pay)}
        return render(request, "suppliers_app_.html", context=data_h)
    elif request.method == "POST" and request.POST.get("add"):
        message_empty = {"message_empty": "Поля не могут быть пустыми!"}
        data = request.POST.get
        name = data("name")
        pay_def = data("pay_def")
        if name and pay_def:
            SuppliersModel.objects.create(name=f"{name}", payment_deferment=f"{pay_def}")
            return redirect("suppliers")
        else:
            return render(request, "suppliers_app_.html", context=message_empty)
    elif request.method == "POST" and request.POST.get("del"):
        message = {"message": "Выбранный поставщик удален!!!"}
        message_empty = {"message_empty": "Поля не могут быть пустыми!"}
        data = request.POST.get
        del_name = data("del_name")
        if del_name:
            d = SuppliersModel.objects.filter(name=del_name)
            d.delete()
            return render(request, "suppliers_app_.html", context=message)
        else:
            return render(request, "suppliers_app_.html", context=message_empty)

    elif request.method == "POST" and request.POST.get("put"):
        message = {"message": "Выбранный поставщик обнавлен!!!"}
        message_empty = {"message_empty": "Поля не могут быть пустыми!"}
        message_err = {"message_err": "Проверьте правильность вводимой информации!"}
        data = request.POST.get
        put_name = data("put_name")
        name = data("name")
        pay_def = data("pay_def_put")
        if put_name and name and pay_def:
            try:
                s = SuppliersModel.objects.get(name=f"{put_name}")
                s.name = f"{name}"
                s.payment_deferment = f"{pay_def}"
                s.save()
                return render(request, "suppliers_app_.html", context=message)
            except:
                return render(request, "suppliers_app_.html", context=message_err)
        else:
            return render(request, "suppliers_app_.html", context=message_empty)
    return render(request, "suppliers_app_.html")


def production_app(request):
    return render(request, "production_app.html")


def wages_app(request):
    if request.method == "GET":
        form = WagesForm()
        form_html = {"form": form}
        return render(request, "wages_app.html", context=form_html)
    elif request.method == "POST":
        form = WagesForm(request.POST)
        if form.is_valid():
            worker = form.cleaned_data.get("worker")
            date_from = form.cleaned_data.get("date_from")
            date_to = form.cleaned_data.get("date_to")
            days_list = list()
            work_days = ScheduleModel.objects.filter(worker=worker)
            for i in work_days:
                if i.date >= date_from and i.date <= date_to:
                    days_list.append(i)
            delta_list = list()
            for i in days_list:
                delta_list.append(i.delta)
            s = 0
            for i in delta_list:
                s += i
            hours = s / 60
            r_p_h = int(request.user.workersmodel.rate_per_hour)
            print(r_p_h)
            pay = hours * r_p_h
            pay1 = {"pay": pay, "pay_text": "Ваша ЗП за выбраный период составит -", "r": "р."}
            sch1 = WagesModel(**form.cleaned_data, hours=hours, total_wages=pay)
            print(sch1)
            sch1.save()
            return render(request, "wages_app.html", context=pay1)
    return redirect("wages")
