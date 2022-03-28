from datetime import datetime

from django.shortcuts import render, redirect

from Administration.forms import BidForm, ScheduleForm
from Administration.models import BidModel, ScheduleModel


def bid_app(request):
    if request.method == "GET":
        form = BidForm()
        form_html = {"form": form}
        return render(request, "bid_app.html", context=form_html)
    elif request.method == "POST":
        form = BidForm(request.POST)
        print(form)
        if form.is_valid():
            bid_tot = BidModel(**form.cleaned_data)
            print(bid_tot)
            bid_tot.save()
        return redirect("bid")


def schedule_app(request):
    if request.method == "GET":
        ses_user2 = request.user.username
        form = ScheduleForm()
        worker = {"worker": ses_user2, "form": form}
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
            print(df, dt, delta)
            sch1 = ScheduleModel(**form.cleaned_data, worker=request.user, delta=delta)
            print(sch1)
            sch1.save()
        return redirect("schedule")
