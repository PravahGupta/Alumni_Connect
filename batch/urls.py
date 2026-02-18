from django.urls import path
from . import views

urlpatterns = [
    path("batchlist", views.batch_list, name="batch_list"),
]