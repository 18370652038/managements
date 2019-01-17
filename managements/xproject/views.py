# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import *
import json
import datetime

@login_required
def index(request):
    request.session['user'] = request.user.username
    request.session['time'] = str(datetime.datetime.now())
    current_user = request.user
    return render(request, 'xproject/index.html',locals())




@login_required
def transaction(request):
    if request.method == 'POST':
        return render(request,'xproject/subclass_details.html',locals())
    else:
        subclass_s = models.subclass_details.objects.all()
        paginator = Paginator(subclass_s,10000)
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

@login_required
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
                'endtime':timezone.localtime(value=subclass.endtime).strftime("%Y-%m-%d %H:%M")
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
        return render(request,'xproject/subclass_all.html',locals())
    else:
        return render(request,'xproject/subclass_all.html',locals())


@login_required
def DeviceInf(request):
    username = request.user.username
    members = models.DeviceInfo.objects.all()
    if request.user.is_superuser:
        members = models.DeviceInfo.objects.all()
        for member in members:
            member.endtime = member.subclass_details_set.all().order_by('-id')[:1][0].endtime
            member.count = len(member.subclass_details_set.all())
    return render(request,'xproject/equipment_all.html',locals())
    pass

@login_required
def DeviceInf_ajax(request):
    if request.method == 'POST':
        Eey = request.POST.get('Eey')
        DeviceID = request.POST.get('DeviceID')
        RegTimes = request.POST.get('RegTimes')
        Organizationname = request.POST.get('Organizationname')
        members = models.DeviceInfo.objects.all()
        if Eey != '' and members != '':
            members = members.filter(Eey=Eey)
        if DeviceID != '' and members != '':
            members = members.filter(DeviceID=DeviceID)
        if RegTimes != '' and members != '' and  not (RegTimes is None):
            # print(RegTimes)
            list = RegTimes.split('-')
            end_date = datetime.date(int(list[0]), int(list[1]), int(list[2])+1)
            print(end_date)
            start_date = datetime.date(int(list[0]), int(list[1]), int(list[2]))
            print(start_date)
            members = members.filter(RegTimes__range=(start_date, end_date))
        if Organizationname != '' and members != '':
            members = members.filter(organization__cname__icontains=str(Organizationname))
        if members != '' and members != [] and not(members is None):
            for member in members:
                member.endtime = member.subclass_details_set.all().order_by('-id')[:1][0].endtime
                member.count = len(member.subclass_details_set.all())
        list = []
        for member in members:
            data = {
                'id': member.id,
                'DeviceID': member.DeviceID,
                'cname': member.organization.cname,
                'RegTimes': timezone.localtime(value=member.RegTimes).strftime("%Y-%m-%d %H:%M"),
                'endtime': timezone.localtime(value=member.endtime).strftime("%Y-%m-%d %H:%M"),
                'count': member.count,
            }
            list.append(data)
        jsons = {'member': list}
        print(jsons)

        return HttpResponse(json.dumps(jsons))
    else:
        return render(request,'xproject/equipment_all.html',locals())

@login_required
def Member(request):
    username = request.user.username
    members = models.NormalUser.objects.filter(username=username)
    if request.user.is_superuser:
        members = models.NormalUser.objects.all()
    return render(request,'xproject/user_all.html',locals())

@login_required
def Member_ajax(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('name')
            nameID = request.POST.get('nameID')
            registertime = request.POST.get('registertime')
            Jurisdiction = request.POST.get('Jurisdiction')
            members = models.NormalUser.objects.all()
            if name !='' and members !='' and name != None:
                members = members.filter(username=name)
            if nameID != '' and members !='':
                members = members.filter(id=nameID)
            if registertime != '' and members != '':
                end_date = datetime.date(2099, 12, 29)
                list = registertime.split('-')
                start_date = datetime.date(int(list[0]), int(list[1]), int(list[2]))
                members = members.filter(endtime__range=(start_date, end_date))
            if Jurisdiction != '' and members != '':
                for member in members:
                    if Jurisdiction == 'administrator':
                        if member.is_superuser:
                            members = members.filter(username=member.username)
                    if Jurisdiction == 'member':
                        if not member.is_superuser:
                            members = members.filter(username=member.username)
            list = []
            for member in members:
                data = {
                    'id':member.id,
                    'name':member.username,
                    'Jurisdiction':'管理员' if member.is_superuser else '会员',
                    'registertime':timezone.localtime(value=member.date_joined).strftime("%Y-%m-%d %H:%M"),
                    'last_login' : timezone.localtime(value=member.last_login).strftime("%Y-%m-%d %H:%M"),
                    'start': '在线' if member.is_authenticated  else '离线',
                }
                list.append(data)
            jsons = {'member':list}
            print(jsons)

            return HttpResponse(json.dumps(jsons))
        else:
            members = models.NormalUser.objects.all()
            return render(request, 'xproject/user_all.html', locals())
    else:
        username = request.user.username
        members = models.NormalUser.objects.filter(username=username)
        return render(request, 'xproject/user_all.html', locals())

def Member_user(request,id):
    if request.user.is_superuser:
        try:
            member = models.NormalUser.objects.get(pk=id)
        except:
            member = ''
        if member != '':
            subclass = member.subclass_details_set.all()
            number = len(subclass)
            sum = 0
            Money = 0
            for i in subclass:
                sum = sum + i.Duration
                Money = Money +i.Money

            if member.is_superuser:
                if request.user.username == member.username:
                    member = member
                    return render(request, 'xproject/user_deta.html', locals())
                else:
                    return redirect('xproject:Member')
            else:
                member = member
                return render(request,'xproject/user_deta.html',locals())
        else:
            return redirect('xproject:Member')

