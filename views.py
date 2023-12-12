from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from django.contrib.auth.models import User
from  django.contrib import auth
from . import forms

def index (request):
    a = loader.get_template('index.html')
    return HttpResponse(a.render())

def about(request):
    b =loader.get_template('about.html')
    return HttpResponse(b.render())

def gallery(request):
    g =loader.get_template('gallery.html')
    return HttpResponse(g.render())

def pricing(request):
    p =loader.get_template('pricing.html')
    return HttpResponse(p.render())

def services(request):
    s =loader.get_template('services.html')
    return HttpResponse(s.render())

def contact(request):
    c =loader.get_template('contact.html')
    return HttpResponse(c.render())

def index1 (request):
    a = loader.get_template('index1.html')
    return HttpResponse(a.render())

def contact1 (request):
    c =loader.get_template('contact1.html')
    return HttpResponse(c.render())

def insert_patient (request):
    if request.method =='POST':
        print("post")
        if request.POST.get('Name') and request.POST.get('diagnosis') and request.POST.get('number'):
            print("data")
            post =models.patientmodel()
            post.Name =request.POST.get('Name')
            print(post.Name)
            post.diagnosis =request.POST.get('diagnosis')
            post.number =request.POST.get('number')
            post.save()
            return HttpResponse("SAVE DATA")
        else:
            return HttpResponse('ERROR')
    else:
        template =loader.get_template('contact.html')
        return HttpResponse(template.render())

def edit_emp(request,id):
    data =models.patientmodel.objects.get(id=id)
    a = loader.get_template('edit.html')
    return HttpResponse(a.render({'patient_data':data}))

def patient(request):
    data =models.patientmodel.objects.all()
    a =loader.get_template('patient.html')
    return HttpResponse(a.render({'patient_data':data}))


def update_emp(request,id):
    data = models.patientmodel.object.get(id=id)
    data.Name = request.POST.get('Name')
    data.diagnosis = request.POST.get('diagnosis')
    data.number = request.POST.get('number')
    data.save()
    return HttpResponse("updated")

def patienttable(request):
    data = models.patientmodel.object.all()
    d =loader.get_template('patienttable.html')
    return HttpResponse(d.render({'patient_data':data}))


def register(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST['username'])
                return HttpResponse("user already exists")
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password'],
                                                email=request.POST['email'])
                auth.login(request, user)
                return HttpResponse("Register successfully")
        else:
                return HttpResponse("PASSWORD DOES NOT MATCH")
    else:
        a = loader.get_template('register.html')
        return HttpResponse(a.render())


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['username'],
                                 password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            a = loader.get_template('login.html',{'error':"Login successfully"})
            return HttpResponse(a.render())
        else:
            return HttpResponse('login.html',{'error':"Username and password is wrong"})
    else:
        a = loader.get_template('login.html')
        return HttpResponse(a.render())




def patients(request):
    if request.method == "POST":
        form = forms.PatientsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("DATA ADD")
            except:
                return HttpResponse("error")
        else:
            return HttpResponse("error")
    else:
        a = loader.get_template('createform.html')
        return HttpResponse(a.render())

# Create your views here
