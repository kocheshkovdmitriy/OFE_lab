from django.urls import path

from lab import views

app_name = 'lab'

urlpatterns = [
    path('', views.Mainpage.as_view(), name='mainpage'),
    path('/class5', views.Lab5Class.as_view(), name='all5class'),
    path('/class6', views.Lab6Class.as_view(), name='all6class'),
    path('/class7', views.Lab7Class.as_view(), name='all7class'),
    path('/class8', views.Lab8Class.as_view(), name='all8class'),
    path('/class9', views.Lab9Class.as_view(), name='all9class'),
    path('/class10', views.Lab10Class.as_view(), name='all10class'),
    path('/class11', views.Lab11Class.as_view(), name='all11class'),
    path('/allworks', views.AllWorks.as_view(), name='allworks'),
    #path('about/', views.About.as_view(), name='about'),
    ]