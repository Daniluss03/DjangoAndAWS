from django.shortcuts import render,redirect

from .forms import UserForm


# Create your views here.


def index(request):
    return render(request,'index.html')


def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('views/login')
        
    context={'form':form}
    return render(request,'register.html',context=context)
    



def dashboard(request):
    return render(request,'dashboard.html')


def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')
