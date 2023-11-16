from django.shortcuts import render

def register_view(request):
    render(request, 'clients/pages/register_view.html')