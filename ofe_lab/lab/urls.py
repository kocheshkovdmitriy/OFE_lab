from django.urls import path

from lab import views

app_name = 'lab'

urlpatterns = [
    path('', views.Mainpage.as_view(), name='mainpage'),
    path('allworks', views.AllWorks.as_view(), name='allworks'),
    path('work/<pk>/', views.Work.as_view(), name='work'),

    path('protocols_work/<pk>', views.Protocols_work.as_view(), name='protocols_work'),
    path('protocols_accept/', views.Accept_protokols.as_view(), name='protocols_accept'),
    path('protocols/download/<pk>', views.download_file_view, name='download'),
    path('protocols/protocol_edit/<pk>', views.edit_protocol, name='protocol_edit'),
    path('protocols/protocol_delete/<pk>', views.delete_protocol, name='protocol_delete'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]