"""onlinesallperchage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='page.html'),name = 'main'),
    path('register/',TemplateView.as_view(template_name='reg.html'),name ='reg'),
    path('save/',views.saveuser,name='saveuser'),
    path('loginpage/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('cheklogin/',views.cheklogin,name = 'cheklogin'),
    path('loginmain/',TemplateView.as_view(template_name='eg.html'),name = 'loginmain'),
    path('loginhome/',views.loginHome,name='home'),
    #path('Sellpage/',TemplateView.as_view(template_name='sell.html',{'data':}),name ='sell'),
    path('selling',views.selling,name = 'sell'),
    path('savepro',views.savepro,name='savepro'),

    path('askquation/',views.ask,name = 'ask'),

    path('buyingproduct/',views.buypro,name='buypro'),

    path('messageproduct/',views.messageProduct,name='msg'),

    path('Messages_from_Customers/',views.custmsg,name = 'custmsg'),

    path('ProductReplyMessage/',views.proreplymsg,name ='proreplymsg')
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)