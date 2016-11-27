from django.shortcuts import render, redirect
from .models import Appt
from ..login_reg_app.models import User
from django.contrib import messages
from datetime import datetime

def index(request):
    context = {
        'today': datetime.now(),
        'user': User.objects.get(id=request.session['user_id']),
        'today_appts': Appt.objects.filter(date=datetime.today()).order_by('time'),
        'other_appts': Appt.objects.all().exclude(date=datetime.today()).order_by('date', 'time'),
    }
    return render(request, "belt_app/index.html", context)

def add_appt(request):
    res = Appt.objects.validate(request.POST)

    if res['added']:
        Appt.objects.create(date=request.POST['date'], time=request.POST['time'], tasks=request.POST['tasks'], status="Pending", user_appt=User.objects.get(id=request.session['user_id']))
    else:
        for error in res['errors']:
            messages.error(request, error)
        return redirect('belt_app:index')

    return redirect("belt_app:index")

def show(request, id):
    context = {
        'appt_info': Appt.objects.filter(id=id)
    }
    return render(request, "belt_app/show.html", context)

def update(request, id):
    res = Appt.objects.validate(request.POST)

    if res['added']:
        new_appt = Appt.objects.get(id=id)
        new_appt.date = request.POST['date']
        new_appt.time = request.POST['time']
        new_appt.tasks = request.POST['tasks']
        new_appt.status = request.POST['status']
        new_appt.user_appt = User.objects.get(id=request.session['user_id'])
        new_appt.save()
    else:
        for error in res['errors']:
            messages.error(request, error)

    return redirect("belt_app:index")

def destroy(request, id):
    Appt.objects.get(id=id).delete()
    return redirect("belt_app:index")

def logoff(request):
    request.session.clear()
    return redirect("login_reg:index")
