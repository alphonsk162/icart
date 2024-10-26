from django.shortcuts import render,redirect
from . models import Customer
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib  import messages

# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('account')
def account(request):
    context={}
    context['click']=False
    if request.POST and "register" in request.POST:
        context['click']=True
        try:
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            address=request.POST.get("address")
            phone=request.POST.get("phone")
        
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success_message="User registered successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Try another username"
            messages.error(request,error_message)
    if request.POST and "login" in request.POST:
        context['click']=True
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password.')
        
    return render(request,'account.html',context)