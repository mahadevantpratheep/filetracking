from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('apply', views.apply, name='apply'),
    path('permission_granted', views.permission_granted, name='permission_granted'),
    path('logout', views.logout, name='logout'),
    path('dashboard_user', views.dashboard_user, name='dashboard_user'),
    path('accept_request/<int:product_id>/', views.accept_request),
    path('reject_request/<int:product_id>/', views.reject_request),
    path('dashboard_fac', views.dashboard_fac, name='dashboard_fac'),
    path('edit_user_profile', views.edit_user_profile, name='edit_user_profile'),
    path('change_password', views.change_password, name='change_password'),
]
