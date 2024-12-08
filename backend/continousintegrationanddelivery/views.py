from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm,UpdateUserForm
from . models import Profile
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User

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
    


@login_required(login_url='login')
def dashboard(request):
    profile_pic=Profile.objects.get(user=request.user)
    context={'profilepic':profile_pic}
    return render(request,'dashboard.html',context=context)


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
def profile_management(request):
    Form=UpdateUserForm(instance=request.user)
    if request.method=='POST':
        Form=UpdateUserForm(request.POST,instance=request.user)
        if Form.is_valid():
            Form.save()
            return  redirect("dashboard")
    context={'Form':Form}
    return render(request,'profile.html',context=context)



@login_required(login_url='login')
def delete_Account(request):
    if request.method=='POST':
        deleteUser=User.objects.get(username=request.user)
        deleteUser.delete()
    return render(request,'deleteaccount.html')