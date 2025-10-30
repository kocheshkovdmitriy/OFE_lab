from django.urls import path
from guide import views

app_name = 'guide'

urlpatterns = [
    path('article/<pk>/', views.ArticlesFromSection.as_view(), name='article'),
    ]