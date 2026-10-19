from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/add/', views.food_add, name='food_add'),
    path('foods/update/<int:food_id>/', views.food_update, name='food_update'),
    path('foods/delete/<int:food_id>/', views.food_delete, name='food_delete'),
]