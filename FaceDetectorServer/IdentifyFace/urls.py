from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verify_face', views.verify_face, name='verify_face'),
    path('log_face', views.log_face, name='log_face'),
    path('add_student/', views.CreateStudentView.as_view(), name='add_student')
]