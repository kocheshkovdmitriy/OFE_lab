from django.urls import path

from lab import views

app_name = 'lab'

urlpatterns = [
    path('', views.Mainpage.as_view(), name='mainpage'),
    path('/allworks', views.AllWorks.as_view(), name='allworks'),
    path('work/<pk>/', views.Work.as_view(), name='work'),
    ]