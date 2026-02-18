from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('profile/', views.profile_view, name='my_profile'),
    path('update_profile', views.update_profile, name="update_profile"),
    # path('request_status_change', views.statuschange, name="request_status_change"),
]