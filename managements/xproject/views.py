from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime


# Create your views here.
@login_required
def index(request):
    current_user = request.user
    return render(request, 'xproject/index.html')




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

@login_required
def subclass_edit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        text = models.subclass_details.objects.get(pk=id)
        text = {
            'number':text.number,
            'name':text.name,
            'Devicename':text.Devicename,
            'Areaname':text.Areaname,
            'Devicenumber':text.Devicenumber,
            'State':text.State,
            'Type':text.Type,
            'Money':text.Money,
            'Duration':text.Duration,
            'paymenttime':text.paymenttime,
            'endtime':text.endtime,
            'POnumber':text.POnumber,
            'Remarks':text.Remarks
        }
        form = editForm(text)
        if form.is_valid():
            return render(request,'xproject/subclass_edit.html',locals())
        form = editForm()
        return render(request,'xproject/subclass_edit.html',locals())

    else:
        form = editForm()
        return render(request,'xproject/subclass_edit.html',locals())

@login_required
def update(request):
    if request.method=='POST':
        id = request.POST.get('id')
        number = request.POST.get('number')
        name = request.POST.get('name')
        Devicename = request.POST.get('Devicename')
        Areanam = request.POST.get('Areanam')
        Devicenumber = request.POST.get('Devicenumber')
        State = request.POST.get('State')
        Type = request.POST.get('Type')
        Money = request.POST.get('Money')
        Duration = request.POST.get('Duration')
        paymenttime = request.POST.get('paymenttime')
        endtime = request.POST.get('endtime')
        POnumber = request.POST.get('POnumber')
        Remarks = request.POST.get('Remarks')
        text = models.subclass_details.objects.get(pk=id)
        if number == '':
            error = "number 不能为空"
            return render(request,'xproject/subclass_edit.html',locals())

