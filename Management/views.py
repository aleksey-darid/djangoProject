import datetime

from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet

from Administration.models import ScheduleModel
from .forms import SupplyForm, SuppliersForm, ProductionForm, WagesForm
from .models import SuppliersModel, ProductionModel, SupplyModel, WagesModel


def supply_app(request):
    if request.method == "GET":
        dat = SupplyModel.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 4:
                new_dat.append(i)
            elif count == 6:
                new_dat.append(i)
            elif count == 7:
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")
        list1 = {"list1": new_dat2}
        form = SupplyForm()
        supply_list = {"supply_list": new_dat2, "form": form}
        return render(request, "supply_app.html", context=supply_list)
    elif request.method == "POST":
        form = SupplyForm(request.POST)
        if form.is_valid():
            sch1 = SupplyModel(**form.cleaned_data)
            print(sch1)
            sch1.save()
        return redirect("supply")


def suppliers_app(request):
    if request.method == "GET":
        dat = SuppliersModel.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 3:
                new_dat.append(i)
            elif count == 4:
                # new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")

        suppliers_list = {"suppliers_list": str(new_dat2)}
        return render(request, "suppliers_app.html", context=suppliers_list)

    elif request.method == "POST":
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми."}
        message = {"message": "Поставщик добавлен."}
        data = request.POST.get
        print(data)
        name = data("name")
        print(name)
        pay_def = data("pay_def")
        print(pay_def)

        count_name = 0
        for _ in name:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "suppliers_app.html", context=error_message_empty)

        count_name = 0
        for _ in pay_def:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "suppliers_app.html", context=error_message_empty)

        new_supplier = SuppliersModel.objects.create(name=f"{name}", payment_deferment=f"{pay_def}")
        new_supplier.save()
        return render(request, "suppliers_app.html", context=message)
    return render(request, "suppliers_app.html")


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
