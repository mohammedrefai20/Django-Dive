from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='instructors_index'),
    path('<int:pk>/', views.detail, name='instructor_detail'),
]
