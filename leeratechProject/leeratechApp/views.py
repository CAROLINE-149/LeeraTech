from django.shortcuts import render

# Create your views here.

def home(request):
    context = {} #dict that will hold out data
    return render(request, 'leeratechApp/home.html', context)

