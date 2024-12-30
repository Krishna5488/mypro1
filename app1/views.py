from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def home(request):
    v='This is Home Page'
    return render(request,'home.html',{'data':v})

def login(request):
    l='This is login Page'
    return render(request,'login.html',{'data1':l})

def signup(request):
    return render(request,'signup.html') 

from .forms import StudentForm

def insert(request):
    st=StudentForm
    if request.method == 'POST':
        s=StudentForm(request.POST)
        if s.is_valid:
            s.save()
            # return HttpResponse("<h1>form is Sbmitted<h1>")
            return redirect('display')

    return render(request,'insert.html',{'form':st})

from .models import Student
def display(request):
    v=Student.objects.all()
    return render(request,'display.html',{'data':v})
