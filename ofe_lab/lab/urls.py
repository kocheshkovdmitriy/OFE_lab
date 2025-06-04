from django.urls import path

from lab import views

app_name = 'lab'

urlpatterns = [
    path('', views.Mainpage.as_view(), name='mainpage'),
    path('allworks', views.AllWorks.as_view(), name='allworks'),
    path('work/<pk>/', views.Work.as_view(), name='work'),
    path('decisions_work', views.Decisions_work.as_view(), name='decisions_work'),

    path('decision/download/<pk>', views.download_file_view, name='download'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]