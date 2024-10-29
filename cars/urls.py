from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.cadastro_veiculos, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('car/<int:id>', views.car, name='car'),
    path('criar_conta/', views.criar_conta, name='criar_conta'),
]
