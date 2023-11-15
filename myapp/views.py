from django.shortcuts import render

def home(request):
    return render(request, 'myapp/pages/home.html')  

def finalpage(request, cargroup):
    return render(request, 'myapp/pages/finalpage.html') 

