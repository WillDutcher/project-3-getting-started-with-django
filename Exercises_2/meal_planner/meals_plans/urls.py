"""Defines URL patterns for meals_plans."""

from django.urls import path

from . import views

app_name = 'meals_plans'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all days.
    path('days/', views.days, name='days'),
    # Detail page for a single day.
    path('days/<int:day_id>/', views.day, name='day'),
    # Page for adding a new meal.
    path('new_meal/<int:day_id>/', views.new_meal, name='new_meal'),
    # Page for editing a meal.
    path('edit_meal/<int:meal_id>/', views.edit_meal, name='edit_meal'),
]
