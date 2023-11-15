from django.urls import path
from . import views # . representa a pasta atual

urlpatterns = [
    path('', views.home, name="myapp-home"),
    path('finalpage/<slug:cargroup>/', views.finalpage, name="myapp-finalpage")
]