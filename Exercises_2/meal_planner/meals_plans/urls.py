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
]
