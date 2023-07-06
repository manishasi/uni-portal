from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_university_data,name='upload_university_data'),
]