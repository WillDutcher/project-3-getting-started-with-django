from django.shortcuts import render

from .models import Day

def index(request):
    """The home page for Meal Plans."""
    return render(request, 'meals_plans/index.html')

def days(request):
    """Show all pizzas."""
    days = Day.objects.order_by('date_added')
    context = {'days': days}
    return render(request, 'meals_plans/days.html', context)

def day(request, day_id):
    """Show a single topic and all its entries."""
    day = Day.objects.get(id=day_id)
    meals = day.meal_set.order_by('-date_added')
    context = {'day': day, 'meals': meals}
    return render(request, 'meals_plans/day.html', context)
