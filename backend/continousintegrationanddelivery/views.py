from django.shortcuts import render,redirect

from .forms import UserForm,LoginForm

from . models import Profile

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate,login


from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


def index(request):
    return render(request,'index.html')


def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            current_user=form.save(commit=False)
            form.save()

            profile=Profile.objects.create(user=current_user)
            return redirect('login')
        
    context={'form':form}
    return render(request,'register.html',context=context)
    

@never_cache  
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')


def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get(('username'))
            password=request.POST.get(('password'))

            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
    context={'form':form}
    return render(request,'login.html',context=context)





def user_logout(request):
    auth.logout(request)
    return redirect('login')
    



@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')
