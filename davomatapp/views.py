from django.shortcuts import render,redirect
from davomatapp.models import Xodim,Davomat
from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def xodim_list(request):
    xodimlar=Xodim.objects.all()
    return render(request,'xodimlar/xodim_list.html',{'xodimlar':xodimlar})


def xodim_create(request):
    if request.method=='POST':
        ism=request.POST.get('ism')
        familiya=request.POST.get('familiya')
        lavozimi=request.POST.get('lavozimi')
        bolim=request.POST.get('bolim')
        telefon_raqami=request.POST.get('telefon_raqami')


        Xodim.objects.create(
            ism=ism,
            familiya=familiya,
            lavozimi=lavozimi,
            bolim=bolim,
            telefon_raqami=telefon_raqami
        )


        return redirect('xodim_list')
    return render(request,'xodimlar/xodim_create.html')




def xodim_update(request,id):
    xodim=Xodim.objects.get(id=id)
    if request.method=='POST':
        xodim.ism=request.POST.get('ism')
        xodim.familiya=request.POST.get('familiya')
        xodim.lavozimi= request.POST.get('lavozimi')
        xodim.bolim= request.POST.get('bolim')
        xodim.telefon_raqami=request.POST.get('telefon_raqami')
        xodim.save()
        return redirect('xodim_list')
    return render(request,'xodimlar/xodim_update.html',{'xodim':xodim})




def xodim_delete(request,id):
    xodim=Xodim.objects.get(id=id)
    xodim.delete()
    return redirect('xodim_list')


def profile(request):
    return render(request,'xodimlar/profile.html')





def davomat(request):
    if request.method=='POST':
        xodim_id=request.POST.get('xodim_id')
        if xodim_id:
            xodim=Xodim.objects.get(id=xodim_id)
            Davomat.objects.create(xodim=xodim)
            xodim.save()
    davomat=Davomat.objects.all()
    xodim=Xodim.objects.all()
    context={
        'davomatlar':davomat,
        'xodim':xodim
    }
    return render(request,'davomat/davomat.html', context)




def registerator(request):
    if request.method=='POST':
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password')

        )
        return redirect('login_user')
    return render(request,'login/login.html')



def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user :
            login(request, user)
            return redirect('xodim_list')
        else:
            return render(request,'error')

    return render(request,'login/login.html')

def log_out(request):
    logout(request)
    return redirect('login_user')


def error(request):
    return render(request, 'login/error.html')














def profile(request):
    return render(request, 'xodimlar/profile.html')







def index(request):
    return render(request, 'index.html')





