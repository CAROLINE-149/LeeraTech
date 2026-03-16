from django.shortcuts import render

# Create your views here.

def home(request):
    context = {} #dict that will hold out data
    return render(request, 'leeratechApp/home.html', context)

def features(request):
    context={}
    return render(request, 'leeratechApp/features.html', context)

def about(request):
    context={}
    return render(request, 'leeratechApp/about.html',context)

def solutions(request):
    context={}
    return render(request, 'leeratechApp/solutions.html', context)

def pricing(request):
    context={}
    return render(request, 'leeratechApp/pricing.html',context)

def contact(request):
    context={}
    return render(request, 'leeratechApp/contact.html',context)