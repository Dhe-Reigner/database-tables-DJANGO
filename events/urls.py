
from django.urls import path
from .views import  home

urlpatterns = [
     path('', home,name='home'),
     path('<str:month>/<int:year>/', home,name='home'),
     
]
