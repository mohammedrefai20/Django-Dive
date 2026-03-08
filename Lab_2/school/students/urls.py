from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='students_index'),
    path('<int:pk>/', views.detail, name='student_detail'),
]
