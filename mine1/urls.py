"""mine1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1 import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',TemplateView.as_view(template_name='page.html'),name = 'main'),
    path('register/',TemplateView.as_view(template_name='registor.html'),name ='register'),
    path('saveuser',views.saveuser,name='saveuser'),
    path('singup/',TemplateView.as_view(template_name='singup.html'),name ='singup'),
    path('checkuser/',views.checkuser,name ='checkuser'),
    path('adminlogin/',TemplateView.as_view(template_name='admin.html'),name='adminlog'),

    path('userlogin/',TemplateView.as_view(template_name='user/usermain.html'),name = 'userlog'),
    path('sell/',TemplateView.as_view(template_name='user/sell.html'),name='sell'),
    path('savepro/',views.savepro,name = 'savepro'),
    path('buy/',TemplateView.as_view(template_name='user/buy.html'),name ='buy'),
    path('question/',TemplateView.as_view(template_name='user/question.html'),name ='question')
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)