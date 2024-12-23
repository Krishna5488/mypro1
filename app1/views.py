from django.shortcuts import render

# Create your views here.

def home(request):
    v='This is Home Page'
    return render(request,'home.html',{'data':v})

def login(request):
    l='This is login Page'
    return render(request,'login.html',{'data1':l})

def signup(request):
    return render(request,'signup.html') 