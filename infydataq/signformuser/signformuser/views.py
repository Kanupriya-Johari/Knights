from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth import login, logout
import re
from .models import FileUpload
import pandas as pd
from django.shortcuts import redirect

   



def signnewuser(request):
    if request.method=="POST":
        if request.POST.get('username')[0].islower():
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The Username should start with uppercase letter...'})
        if int(request.POST.get('age'))<20:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The age must be greater than 20...'})
        regex = r'\b[A-Za-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if( not (re.fullmatch(regex, request.POST.get('email')))):
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'please enter valid Email...'})
        if len(request.POST.get('password1'))<8:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The Password length should be minimum 8 characters...'})
        elif request.POST.get('password1')==request.POST.get('password2'):
          try:
            saveuser=User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password1'))
            saveuser.save()
            return render(request,'Signup.html',{'form':UserCreationForm(),'info':'The User ' +request.POST.get('username')+' is saved successfully...'})
          except IntegrityError:
                return render(request,'Signup.html',{'form':UserCreationForm(),'error':'The User ' +request.POST.get('username')+' already exists...'})
        else:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error':'The passwords are not matching'})
    else:
        return render(request,'Signup.html',{'form':UserCreationForm})


def loginuser(request):
    
    if request.method=="POST":
        loginsuccess=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password')) 
        
        if loginsuccess is None:
            return render(request,'Login.html',{'form':AuthenticationForm(),'error':'The username and password are wrong..'})
        else:
            login(request,loginsuccess)
            return redirect('Welcomepage')
    else:
        return render(request,'Login.html',{'form':AuthenticationForm()})  

def loginAdmin(request):
    return redirect("http://127.0.0.1:8000/admin/login/?next=/admin/")        

def home(request): 
    return render(request,'Page1.html')    

def Welcomepage(request):
    return redirect('index1')       

def logoutpage(request):
    if request.method=="POST":
        logout(request)
    else:    
        return redirect('loginuser')
    
def adminlogin(request):
    return render(request,'ADMINLOGIN.html')
def adminsignup(request):
    return render(request,'ADMINSIGNUP.html')
def adminwelcome(request):
    return render(request,'ADMINWELCOME.html')
    
def sideview(request):
    return render(request,'sideview.html')
def userdetails(request):
    return render(request,'userdetails.html')
def uploadedfiledetails(request):
    return render(request,'uploadedfiledetails.html')
def index1(request):
    return render(request,'index1.html')

def index(request):
    if request.method == 'POST':
        file2 = request.FILES["file"]
        csv=pd.read_csv(file2)
        print(csv.head())
        df=csv.dropna(axis=0)
        print(csv.to_string())
        document=FileUpload.objects.create(file=file2)
        document.save()
        df.to_csv('cleaned_file.csv')
        return HttpResponse("your file was saved")
    else:
        return render(request, 'index.html')
