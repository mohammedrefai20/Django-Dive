from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='courses_index'),
    path('<int:pk>/', views.detail, name='course_detail'),
]
