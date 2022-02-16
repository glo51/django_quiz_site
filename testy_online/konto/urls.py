from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'konto'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='konto/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='konto/logout.html'), name='logout'),
    path('', views.profile, name='profile'),
    path('send_test/<int:test_id>/', views.send_test, name='send_test'),
    path('result/<int:score>/<int:max_score>/', views.get_result, name='result')
]
