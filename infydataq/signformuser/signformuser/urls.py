"""signformuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.signnewuser,name="signnewuser"),                                                 #'register/'
    path('loginuser/',views.loginuser,name="loginuser"),
    path('loginAdmin/',views.loginAdmin,name="loginAdmin"),
    path('Welcome/',views.Welcomepage,name="Welcomepage"),
    path('Logout/',views.logoutpage,name="logoutpage"),
    path('',views.home,name="home"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminsignup/',views.adminsignup,name="adminsignup"),
    path('adminwelcome/',views.adminwelcome,name="adminwelcome"),
    path('sideview/',views.sideview,name="sideview"),
    path('userdetails/',views.userdetails,name="userdetails"),
    path('index/',views.index,name="index"),
    path('uploadedfiledetails/',views.uploadedfiledetails,name="uploadedfiledetails"),
    path('index1/',views.index1,name="index1"),
     path('fileRetrospection/',views.fileRetrospection,name="fileRetrospection")

    #path('FileUploadView/',views.FileUploadView,name="FileUploadView"),
    # path('Logout',views),
    #  path('', views.home)
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
