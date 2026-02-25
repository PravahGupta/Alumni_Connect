from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='my_profile'),
    path('see_profile', views.see_profile, name='see_profile'),
    path('update_profile', views.update_profile, name="update_profile"),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('search', views.search, name="search"),
    path('alumni_dir', views.alumni_dir, name='alumni_dir'),
    # path('request_status_change', views.statuschange, name="request_status_change"),
]