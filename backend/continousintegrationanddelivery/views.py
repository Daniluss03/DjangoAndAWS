from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm,UpdateUserForm,updatePicture
from . models import Profile
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.conf import settings



from django.core.mail import send_mail

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
            send_mail(
                subject="Welcome to Danilus Web Application",
                message="Hello! Welcome to Daniluss Web application.We're excited to have you here",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[current_user.email],
                fail_silently=False,
            )
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
    

@login_required(login_url='my-login')
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)
    profile_form = updatePicture(instance=profile)

    if request.method == 'POST':
        if 'update_user' in request.POST:  # Verifica si se envió el formulario de usuario
            user_form = UpdateUserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect("dashboard")  # Redirige después de guardar el usuario

        elif 'update_picture' in request.POST:  # Verifica si se envió el formulario de imagen
            profile_form = updatePicture(request.POST, request.FILES, instance=profile)
            print(profile_form)           
            if profile_form.is_valid():
                profile_form.save()
                print(profile_form)
                return redirect("dashboard")  # Redirige después de guardar la imagen

    context = {'Form': user_form, 'profile_form': profile_form}
    print(context)
    return render(request, 'profile.html', context=context)



@login_required(login_url='login')
def delete_Account(request):
    if request.method=='POST':
        deleteUser=User.objects.get(username=request.user)
        deleteUser.delete()
    return render(request,'deleteaccount.html')



    