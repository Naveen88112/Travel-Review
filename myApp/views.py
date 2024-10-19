from django.shortcuts import render

def home(request):
    context={}
    return render(request, "myApp/home.html", context)

def about(request):
    context={}
    return render(request, "myApp/about.html", context)

def contact(request):
    context={}
    return render(request, "myApp/contact.html", context)

def destinations(request):
    context={}
    return render(request, "myApp/destinations.html", context)

def reviews(request):
    context={}
    return render(request, "myApp/reviews.html", context)

