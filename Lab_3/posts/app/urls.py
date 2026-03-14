from django.urls import path
from . import views
from app.views import PostView

urlpatterns = [
    path('', views.PostView.as_view(), name='post-list'),
]
