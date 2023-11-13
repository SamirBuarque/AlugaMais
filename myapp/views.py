from django.shortcuts import render

def home(request):
    return render(request, 'myapp/pages/home.html')  

def teste(request, cargroup):
    return render(request, 'myapp/pages/finalpage.html') 