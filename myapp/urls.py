from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('upload/', views.upload_images, name='upload_images'),
]