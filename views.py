from django.http import HttpResponse
from django.shortcuts import render
from .models import User


# Create your views here.
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        age = request.POST.get('age')
        try:
            User.objects.create(name=uname,age=age)
        except:
            return HttpResponse('注册失败')
        return HttpResponse('注册成功')