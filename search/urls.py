from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.results, name='results'),
    path('contact/',views.contact,name='contact'),
    path('result/<int:id>/',views.detailed,name='detail')
]
