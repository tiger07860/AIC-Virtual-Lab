from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list', views.experiments, name="experiments"),
    path('experiment/<str:arg>/', views.experiment, name="experiment"),
    path('simulation/<str:arg>/', views.simulation, name="simulation"),
]
