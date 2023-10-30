from django.urls import path
from myapp.views import home, test, contato

urlpatterns = [
    path('', home),
    path('test/', test),
    path('contato/', contato)
]