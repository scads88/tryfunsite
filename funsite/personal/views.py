from django.shortcuts import render


def index(request):
    return render(request, "personal/home.html")
# Create your views here.


def contact(request):
    return render(request, "personal/basic.html", {"content":["if you would like to contact me", 
                                                              "please email me,", 
                                                              "sup@gmail.com" ]})
#request, #what you're gunna render, #optional dictionary that you can store things