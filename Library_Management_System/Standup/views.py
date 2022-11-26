
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Standup.models import Books
# from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
#adding book

def bkf(request):
    if (request.method =='POST'):
        Bname_=request.POST['Bname']
        Bauthor_=request.POST['Bauthor']
        YearofPub_=request.POST['YearofPub']
        Price_=request.POST['Price']
        Page_=request.POST['Page']
        Category_=request.POST['Category']
        data=Books.CustomManager.create(Bname=Bname_,Bauthor=Bauthor_,YearofPub=YearofPub_,Price=Price_,Page=Page_,Category=Category_)
        data.save()
        return redirect("/")
    return render(request,"Standup/bkform.html")

#Displaying allbook

def allbook(self):
    Bk=Books.CustomManager.all()
    bkd={"Bks":Bk}
    return render(self,'Standup/book.html',context=bkd)

#Deleting the Books

def delete(request,id):
    pi=Books.CustomManager.filter(pk=id)
    pi.delete()
    pi.update(is_deleted='y')
    return redirect("/")



#Price Filter

def hightolow(request):
    content={}
    content['Bks']=Books.CustomManager.all_book_in_desc_price()
    return render(request,"Standup/book.html",content)
def lowtohigh(request):
    content={}
    content['Bks']=Books.CustomManager.all_book_in_asce_price()
    return render(request,"Standup/book.html",content)

#Sort By Accordingly

def NonFiction(request):
    content={}
    content['Bks']=Books.CustomManager.filter(Category='NonFiction')
    return render(request,"Standup/book.html",content)
def Fiction(request):
    content={}
    content['Bks']=Books.CustomManager.filter(Category='Fiction')
    return render(request,"Standup/book.html",content)
def Reference(request):
    content={}
    content['Bks']=Books.CustomManager.filter(Category='Reference')
    return render(request,"Standup/book.html",content)
def Edited(request):
    content={}
    content['Bks']=Books.CustomManager.filter(Category='Edited')
    return render(request,"Standup/book.html",content)

def search(request):
    query=request.GET['query']
    data=Books.CustomManager.filter(Bname__icontains=query)
    return render(request,'Standup/search.html',{'data':data})


#Upadte the data

def update(request,id):
    if (request.method =='POST'):
        Bname_form=request.POST['Bname']
        Bauthor_form=request.POST['Bauthor']
        YearofPub_form=request.POST['YearofPub']
        Price_form=request.POST['Price']
        Page_form=request.POST['Page']
        Category_form=request.POST['Category']
        pi=Books.CustomManager.filter(pk=id)
        pi.update(Bname=Bname_form,Bauthor=Bauthor_form,YearofPub=YearofPub_form,Price=Price_form,Page=Page_form,Category=Category_form)
        return redirect('/')
    else:
        content={}
        content['Bks']=Books.CustomManager.get(pk=id)
        return render(request,'Standup/update.html',content)
