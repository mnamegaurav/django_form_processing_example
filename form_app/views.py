from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse

def home(request):
    # request.session.set_test_cookie()
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        file = request.FILES['file']
        FormData.objects.create(name=name,email=email,password=password,file=file)
        return HttpResponse('Success')
    else:
        ajax_form = PracticeForm()
        return render(request,'home.html',{'ajax_form':ajax_form})    

def forms_processing(request):
    if request.method=='POST':
        form = PracticeForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            file = form.cleaned_data['file']
            FormData.objects.create(name=name,email=email,password=password,file=file)
            return redirect('forms_processing')
        else:
            form = PracticeForm()
    else:
        form = PracticeForm()
        return render(request,'form.html',{'form':form})


def model_forms_processing(request):
    if request.method=='POST':
        model_form = PracticeModelForm(request.POST or None,request.FILES or None)
        if model_form.is_valid():
            model_form.save()
            return redirect('model_forms_processing')
        else:
            model_form = PracticeModelForm()
    else:
        model_form = PracticeModelForm()
        return render(request,'model_form.html',{'model_form':model_form})


# def new(request):
#     if request.session.test_cookie_worked():
#         print('cookies worked')
#         request.session.delete_test_cookie()

#     return HttpResponse('<h1>Hey it worked</h1>')