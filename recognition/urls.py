from django.urls import path
from . import views

app_name = 'recognition'

urlpatterns = [
    path('', views.index, name='index'),
    path('recognize/', views.recognize_sign, name='recognize_sign'),
]