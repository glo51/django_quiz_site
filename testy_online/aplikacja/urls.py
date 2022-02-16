from django.urls import path
from . import views


app_name = 'aplikacja'
urlpatterns = [
    path('', views.tests, name='tests'),
    path('<int:test_id>/', views.q_and_a, name='q_and_a')
]
