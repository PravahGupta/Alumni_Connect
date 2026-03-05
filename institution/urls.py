from django.urls import path
from . import views

urlpatterns = [
    path('create-university/', views.create_university, name='create_university'),
    path('create-institution/', views.create_institution, name='create_institution'),
    path('create-program/', views.create_program, name='create_program'),
    path('create-skill/', views.create_skill, name='create_skill'),
    path('create-batch/', views.create_batch, name='create_batch'),

]