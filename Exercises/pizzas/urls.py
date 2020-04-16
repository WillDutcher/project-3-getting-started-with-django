"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    # Page for adding a new pizza.
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    # Page for adding a new topping.
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
]
