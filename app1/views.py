from django.shortcuts import render
from django.contrib import messages
from .models import UserModel,ProductModel
# Create your views here.
def saveuser(request):
    username = request.POST.get('name')
    phonenum = request.POST.get('phonenum')
    email = request.POST.get('email')
    password = str(request.POST.get('psw'))
    cpassword = str(request.POST.get('psw-repeat'))
    print(password,cpassword)
    if password == cpassword:
        UserModel(name =username,contactno=phonenum,password=password,email=email).save()
        messages.success(request,'Successfully Register')
        return render(request,'registor.html')
    else:
        messages.error(request,'Password and Confirm Password are not same')
        return render(request,'registor.html')


def checkuser(request):
    email = request.POST.get('email')
    password = request.POST.get('psw')
    print(email,password)
    try:

        u=UserModel.objects.get(email = email,password = password)
        request.session['status'] = True

        return render(request,'user/sell.html',{'data':u})

    except UserModel.DoesNotExist:
        messages.error(request,'Check Email and Password')
        return render(request,'singup.html')


def savepro(request):
    user = request.GET.get('userid')
    price =request.POST.get('t3')
    t = request.POST.get('t1')
    name = request.POST.get('t2')
    iamge = request.POST['t4']



    ProductModel(userid_id=user,category=t,price=price,pname=name,photo=iamge)
    return None