from django.urls import path
from . import views


urlpatterns = [
    path('soil/', views.soil, name='soil'),
    path('', views.index, name='index'),
    path('addplant/', views.addplant, name='addplant'),
    path('fertilizerchecking/', views.fertilizerchecking, name='fertilizerchecking'),
    path('searchtest/', views.searchtest, name='searchtest'),
    path('searchplant/', views.searchplant, name='searchplant'),
]