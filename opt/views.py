from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from .models import Member
from django.contrib import messages


# Create your views here.
# def members(request):
#     # return HttpResponse('Hello World')
#     temp = loader.get_template('index.html')
#     return HttpResponse(temp.render())

def gadhaDolly(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render())
   
def showAll(request):
    myval = Member.objects.all().values();
    tem = loader.get_template('main.html')
    con = {
        'myva':myval,
        'name': 'Dolly'
    }
    return HttpResponse(tem.render(con,request));

def postData(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        date = request.POST.get('date')
        member = Member(firstname = firstname, lastname = lastname, age = age, addedDate = date)
        member.save()
        messages.success(request, "Data Uploaded.")
    return render(request,'add.html')

def deleteData(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('showAll'))

def updateData(request,id):
    member = Member.objects.get(id=id)
    page = loader.get_template('update.html')
    context = {
        'val':member
    }
    return HttpResponse(page.render(context,request))

def updateRecord(request,id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.age = request.POST['age']
    member.addedDate = request.POST['date']
    member.save()
    return HttpResponseRedirect(reverse('showAll'))