from django.shortcuts import render,redirect
from . import models
from .forms import *


# Create your views here.
def index(request):
    current_user = request.user

    if current_user.is_authenticated():
        return render(request, 'xproject/index.html')
    return redirect('account_login')





def transaction(request):
    # loca = models.subclass_details.objects.all()
    # print(loca)
    return render(request,'xproject/subclass_details.html')
