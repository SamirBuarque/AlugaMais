from django.urls import path
from . import views # . representa a pasta atual

urlpatterns = [
    path('', views.home),
    path('finalpage/<slug:cargroup>/', views.teste)

]