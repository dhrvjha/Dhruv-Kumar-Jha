from django.shortcuts import render
from django.http import HttpResponse
from .url_service import uuid_engine as ueng, check_continue

# Create your views here.
def returnUUID(wsgiObject):
    return (str(wsgiObject).split('/')[2].split('\'')[0])

def voteview(request, factory_id):
    _uuid = returnUUID(request)
    email_flag = ueng.search_id(_uuid)
    if (email_flag == None):
        return HttpResponse("You don't have permission to vote")
    name = email_flag.split('_')[0]
    check_continue.add_to_continue_list(request_uuid=_uuid, email=email_flag)
    htmlrespnse = '<a href=\"http://127.0.0.1:8000/vote/'+_uuid +'/continue/\">continue</a>'
    return render(request, 'election/home.html')

def votecontinueview(request, factory_id):
    _uuid = returnUUID(request)
    email_flag = check_continue.get_uuid_from_list(_uuid)
    if email_flag == None:
        return HttpResponse('you cannot vote none')
    email = email_flag[0]
    if email_flag[1]:
        return HttpResponse('you cannot vote time')
    return HttpResponse("votecount",email)

def conductvoteview(request):
    return render(request, 'election/home.html')