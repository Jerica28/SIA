from django.urls import path
from . import views

urlpatterns = [
    # Landing page
    path('', views.home, name='home'),

    # Food management dashboard
    path('foods/', views.food_list, name='food_list'),

    # Add food
    path('foods/add/', views.food_add, name='food_add'),

    # Update food
    path('foods/update/<int:food_id>/', views.food_update, name='food_update'),

    # Delete food
    path('foods/delete/<int:food_id>/', views.food_delete, name='food_delete'),
]