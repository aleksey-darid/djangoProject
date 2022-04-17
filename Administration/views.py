from datetime import datetime
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from Administration.forms import BidForm, ScheduleForm
from Administration.models import BidModel, ScheduleModel
from Administration.serializers import ScheduleSerializer, BidSerializer


class ScheduleView(ModelViewSet):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer


class BidView(ModelViewSet):
    queryset = BidModel.objects.all()
    serializer_class = BidSerializer


def bid_app(request):
    if request.method == "GET":
        form = BidForm()
        form_html = {"form": form}
        return render(request, "bid_app.html", context=form_html)
    elif request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid_tot = BidModel(**form.cleaned_data)
            bid_tot.save()
        return redirect("home")


def schedule_app(request):
    if request.method == "GET":
        ses_user = request.user.username
        form = ScheduleForm()
        look_s = ScheduleModel.objects.filter(worker__username=ses_user)
        look_sc = []
        for i in look_s:
            if i.date.month == datetime.now().month:
                look_sc.append(i)
        worker = {"worker": ses_user, "form": form, "look_sc": look_sc}
        return render(request, "schedule_app.html", context=worker)
    elif request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            df = datetime.strptime(
                str(form.cleaned_data.get("date")) + str(form.cleaned_data.get("time_from")),
                "%Y-%m-%d%H:%M:%S")
            dt = datetime.strptime(str(form.cleaned_data.get("date")) + str(form.cleaned_data.get("time_to")),
                                   "%Y-%m-%d%H:%M:%S")
            delta = (dt - df).seconds / 60
            sch1 = ScheduleModel(**form.cleaned_data, worker=request.user, delta=delta)
            sch1.save()
        return redirect("schedule")
