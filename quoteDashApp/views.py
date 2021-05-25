# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *


def index(request):
    return render(request, "LoginReg.html")

def register(request):
    error = Users.objects.i_am_the_validator(request.POST)

    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")
            

    newuser = Users.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], email = request.POST["eml"], password = request.POST["PW"])

    request.session["UserID"] = newuser.id

    return redirect('/wishes')

def login(request):
    error = Users.objects.loginVal(request.POST)

    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")

    else: 
        user = Users.objects.get(email = request.POST['eml']) 

        request.session["UserID"] = user.id

        return redirect("/wishes")

def newsfeed(request):
    context = {
        'thisusers': Users.objects.get(id=request.session["UserID"]),
        'quotelist': Quotes.objects.all()
    }
    return render(request, "newsfeed.html", context)

def newQuote(request):
    error = Quotes.objects.quoteVal(request.POST)

    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/quotes")

    Quotes.objects.create(author = request.POST["AT"], quote = request.POST["QT"], posted_by = Users.objects.get(id=request.session["UserID"]))
    return redirect("/quotes")

def completedestrution(request, QuoteID):


    c = Quotes.objects.get(id=QuoteID)
    c.delete()

    return redirect("/quotes")

def myAccount(request, UserID):
    

    context = {
        'allusers': Users.objects.get(id=request.session["UserID"])
        
    }
    return render(request, "accpg.html", context)

def updateAccount(request, UserID):
    error = Users.objects.updateVal(request.POST)

    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect(f"/myaccount/{UserID}")

    else:
        c = Users.objects.get(id=request.session["UserID"])
        c.first_name = request.POST['fname']
        c.last_name = request.POST['lname']
        c.email = request.POST['Email']
        c.save()

        return redirect(f"/myaccount/{UserID}")

def postedbyUser(request, UserID):
    context = {
        'userThatsLooking': Users.objects.get(id=request.session["UserID"]),
        'userquotelist': Users.objects.get(id=UserID)
    }
    return render(request, "userQ.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")

def liked(request, QuoteID):
    Users.objects.get(id=request.session["UserID"]).liked_quotes.add(Quotes.objects.get(id=QuoteID))
    return redirect("/quotes")