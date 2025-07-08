from django.shortcuts import render,redirect
from.models import*

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def register(request):
   obj=UserInfo()
   obj.name=request.POST.get("name")
   obj.address=request.POST.get("address")
   obj.address=request.POST.get("address")
   obj.phone_number=request.POST.get("phone_number")
   obj.email=request.POST.get("email")
   obj.save()
   return redirect('registration')
#    return render(request,'success.html',{'name':name,'address':address})

