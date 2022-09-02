from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.

def index(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def bookings(request):
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Booked successfully')

        else:
            return render(request,'bookings.html')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'bookings.html',dict_form)

def doctors(request):
    doc={
            'doctors': Doctors.objects.all()
        }
    return render(request,'doctors.html',doc)

def department(request):

    dept={
        'dept': Departments.objects.all()
    }

    return render(request,'department.html',dept)

def contact(request):

    return render(request,'contact.html')





