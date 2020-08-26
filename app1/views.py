from django.shortcuts import render,redirect,resolve_url
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

from .models import UserModel,ProductModel,ProductMessage

def saveuser(request):
    na = request.POST.get('name')
    ea = request.POST.get('eamil')
    ph = request.POST.get('phonenum')
    ps = str(request.POST.get('psw'))
    ps1 = str(request.POST.get('cpsw'))

    if ps == ps1:
        UserModel(name=na,email=ea,phno=ph,password=ps).save()
        messages.success(request,'Successfully Register Login Here With Your Email and Password')
        return redirect('login')
    else:
        messages.error(request,'Password and Confirm Password are not same')
        return redirect('reg')


def cheklogin(request):
    em = request.POST.get('email')
    pa = request.POST.get('psw')
    try:
        u = UserModel.objects.get(email=em,password=pa)
        #return render(request,'eg.html')
        pm = ProductModel.objects.all()
        return render(request,'eg.html',{'data':u,'product':pm})
    except UserModel.DoesNotExist:
        messages.error(request,'Check Email and Password')
        return redirect('login')


def loginHome(request):
    user = request.GET.get('id')
    u = UserModel.objects.get(usernum=user)
    pm = ProductModel.objects.all()

    return render(request,'eg.html',{'data':u,'product':pm})
# def eg(request):
#     return render(request,'')


def savepro(request):
    type = request.POST.get('t1')
    name = request.POST.get('t2')
    price = request.POST.get('t3')
    dis = request.POST.get('t4')
    image = request.FILES['t5']
    id = request.POST.get('usernum')
    ProductModel(ptype=type,pname=name,price=price,descriptionproduct=dis,image=image,userid_id=id).save()
    messages.success(request,'Product is saved')
    u = UserModel.objects.get(usernum=id)
    hisdata = ProductModel.objects.filter(userid_id=id)

    return render(request,'sell.html',{'data':u,'product':hisdata})




def selling(request):
    user =request.GET.get('id')
    u=UserModel.objects.get(usernum=user)
    hisdata = ProductModel.objects.filter(userid_id= user)

    return render(request,'sell.html',{'data':u,'product':hisdata})


def ask(request):
    user = request.GET.get('id')
    u = UserModel.objects.get(usernum=user)
    return render(request,'ask.html',{'data':u})


def buypro(request):
    productid = request.GET.get('pid')
    user = request.GET.get('id')
    print('product id')
    print(productid)
    print('user id')
    print(user)

    pm = ProductModel.objects.get(id=productid)
    u = UserModel.objects.get(usernum=user)

    data = UserModel.objects.get(usernum=pm.userid_id)

    return render(request,'buyproduct.html',{'product':pm,'data':u,'pp':data})


def messageProduct(request):
    productid = request.GET.get('pid')
    userid = request.GET.get('uid')
    msg = request.GET.get('msg')
    rec = request.GET.get('rec')
    print(productid,userid,msg,rec)
    um = UserModel.objects.get(usernum=userid)
    pm = ProductModel.objects.get(id=productid)
    data = UserModel.objects.get(usernum=rec)
    ProductMessage(customermsg=msg,fromid_id=userid,toid=rec,productid_id=productid).save()
    #messages.success(request,'Message Sent successfully To')
    print('save')
    return render(request,'buyproduct.html',{'data':um,'product':pm,'pp':data,'msg':'Message Sent Successfully To'})


def custmsg(request):
    user = request.GET.get('id')
    to = ProductMessage.objects.filter(toid=user)
    um = UserModel.objects.get(usernum=user)
    fromid = ProductMessage.objects.filter(fromid_id=user)
    return render(request,'showmsg.html',{'msg':to,'data':um,'from':fromid})


def proreplymsg(request):
    user = request.GET['to']
    fr = request.GET['from']
    msg = request.GET['t1']
    pro = request.GET['pro']
    ProductMessage.objects.filter(fromid_id=fr,toid=user,productid_id=pro).update(customerreply=msg)
    print(msg,user)
    return HttpResponse('ok')