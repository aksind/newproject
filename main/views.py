from django.shortcuts import render, redirect
from .models import User1
from django.contrib.auth.models import User
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout


# Create your views here.
def add(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User1(name=nm, email=em, password=ps)
            reg.save()
    else:
        fm=StudentRegistration() 
    stud=User1.objects.all()           
    return render(request,'addshow.html', {'form':fm,'stu':stud})

def edit(request, id):
    if request.method=='POST':
        ed=User1.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=ed)
        if fm.is_valid():
            fm.save()
            return redirect('/add')
        else:
            ed=User1.objects.get(pk=id)
            fm=StudentRegistration(instance=ed)
    return render(request, 'edit.html', {'form':fm})   

def delete(request, id):
    if request.method=='POST':
        de=User1.objects.get(pk=id)
        de.delete()
    return HttpResponseRedirect('/add') 

def home(request):
    return render(request, 'home.html')



def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request, 'signin.html')

def logiN(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('add')
        else:
            return redirect('signin')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('/')