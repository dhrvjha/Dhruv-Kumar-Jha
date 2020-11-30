from django.shortcuts import render
from django.http import HttpResponse
from .url_service import uuid_engine as ueng

# Create your views here.
def home(request):
    ueng.new_id('dhruv_201800528@smit.smu.edu.in')
    _uuid = str(request).split('?')[1][0:36]
    flag = ueng.search_id(_uuid)
    if (flag == None):
        return HttpResponse("You don't have permission to vote")
    name = flag.split('_')[0]
    return HttpResponse("hello there, "+name)

