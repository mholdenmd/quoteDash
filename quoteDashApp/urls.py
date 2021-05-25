from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('quotes', views.newsfeed),
    path('addNewQuote', views.newQuote),
    path('shows/<int:QuoteID>/destory', views.completedestrution),
    path('myaccount/<int:UserID>', views.myAccount),
    path('quotes/<int:UserID>/update', views.updateAccount),
    path('user/<int:UserID>', views.postedbyUser),
    path('logout', views.logout),
    path('liked/<int:QuoteID>', views.liked)
]