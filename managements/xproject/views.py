from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.contrib.auth.decorators import login_required
from .forms import *
import json
import datetime

@login_required
def index(request):
    request.session['user'] = request.user.username
    request.session['time'] = str(datetime.datetime.now())
    print(datetime.datetime.now())
    print(request.session)
    print(request.session.get_expiry_date())
    print(request.user.username)
    print(2)
    current_user = request.user
    return render(request, 'xproject/index.html',locals())




@login_required
def transaction(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        Devicenumber = request.POST.get('Devicenumber')
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        State = request.POST.get("State")
        subclass_s = models.subclass_details.objects.all()
        if starttime != '' and subclass_s != '' or endtime != '' and subclass_s != '':
            start_date = datetime.date(2005, 1, 1)
            end_date = datetime.date(2099, 12, 29)
            if starttime != '':
                list = starttime.split('-')
                start_date = datetime.date(int(list[0]), int(list[1]), int(list[2]))
            if endtime != '':
                list1 = endtime.split('-')
                end_date = datetime.date(int(list1[0]), int(list1[1]), int(list1[2]))
            subclass_s = subclass_s.filter(endtime__range=(start_date, end_date))
        if number != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter(number=number)
            except:
                subclass_s =subclass_s
        if Devicenumber != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter(Devicenumber=Devicenumber)
            except:
                subclass_s = subclass_s
        if starttime != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter()
            except:
                subclass_s = subclass_s
        if State != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter(State=State)
            except:
                subclass_s = subclass_s
        paginator = Paginator(subclass_s,4)
        subclass_s = paginator.page(1)
        return render(request,'xproject/subclass_details.html',locals())
    else:
        subclass_s = models.subclass_details.objects.all()
        paginator = Paginator(subclass_s,4)
        page = request.GET.get('page')
        try:
            page = int(page)
            page = int(page)
        except:
            page = 1
        if page == None :
            page = 1
        print(page)
        try:
            subclass_s = paginator.page(page)
        except PageNotAnInteger:
            subclass_s = paginator.page(1)
        except EmptyPage:
            subclass_s = paginator.page(paginator.num_pages)
        return render(request,'xproject/subclass_details.html',locals())

def transaction_ajax(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        Devicenumber = request.POST.get('Devicenumber')
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        State = request.POST.get("State")
        subclass_s = models.subclass_details.objects.all()
        if starttime != '' and subclass_s != '' or endtime != '' and subclass_s != '':
            start_date = datetime.date(2005, 1, 1)
            end_date = datetime.date(2099, 12, 29)
            if starttime != '':
                list = starttime.split('-')
                start_date = datetime.date(int(list[0]), int(list[1]), int(list[2]))
            if endtime != '':
                list1 = endtime.split('-')
                end_date = datetime.date(int(list1[0]), int(list1[1]), int(list1[2]))
            subclass_s = subclass_s.filter(endtime__range=(start_date, end_date))
        if number != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter(number=number)
            except:
                subclass_s =subclass_s
        if Devicenumber != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter(Devicenumber=Devicenumber)
            except:
                subclass_s = subclass_s
        if starttime != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter()
            except:
                subclass_s = subclass_s
        if State != '' and subclass_s != '':
            try:
                subclass_s = subclass_s.filter(State=State)
            except:
                subclass_s = subclass_s
        list = []
        for subclass in subclass_s:
            date = {
                'id':subclass.id,
                'number': subclass.number,
                'name':subclass.normalUser.username,
                'DeviceID':subclass.deviceInfo.DeviceID,
                'State':subclass.State,
                'Type':subclass.Type,
                'Money':str(subclass.Money),
                'endtime':str(subclass.endtime)
            }
            list.append(date)
        jsonz = {"subclass":list}
        print(jsonz)

        return HttpResponse(json.dumps(jsonz))

@login_required
def subclass_all(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        text = models.subclass_details.objects.get(pk=id)
        price = text.organization.price_set.all()[0].price
        # text = {
        #     'number':text.number,
        #     'name':text.normalUser.username,
        #     'Devicename':text.deviceInfo.DeviceID,
        #     'Areaname':text.organization.cname,
        #     'State':text.State,
        #     'Type':text.Type,
        #     'Money':text.Money,
        #     'Duration':text.Duration,
        #     'paymenttime':text.paymenttime,
        #     'endtime':text.endtime,
        #     'POnumber':text.POnumber,
        # }
        # form = editForm(text)
        # if form.is_valid():
        #     return render(request,'xproject/subclass_edit.html',locals())
        # form = editForm()
        return render(request,'xproject/subclass_all.html',locals())
    else:
        return render(request,'xproject/subclass_all.html',locals())



def DeviceInf(request):
    pass

@login_required
def Member(request):
    username = request.user.username
    members = models.NormalUser.objects.filter(username=username)
    if request.user.is_superuser:
        members = models.NormalUser.objects.all()
    return render(request,'xproject/user_all.html',locals())
