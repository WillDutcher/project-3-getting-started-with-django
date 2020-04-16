from django.shortcuts import render, redirect

from .models import Day
from .forms import MealForm

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

def new_meal(request, day_id):
    """Add a new meal for a particular day."""
    day = Day.objects.get(id=day_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = MealForm()
    else:
        # POST data submitted; process data.
        form = MealForm(data=request.POST)
        if form.is_valid():
            new_meal = form.save(commit=False)
            new_meal.day = day
            new_meal.save()
            return redirect('meals_plans:day', day_id=day_id)

    # Display a blank or invalid form.
    context = {'day': day, 'form': form}
    return render(request, 'meals_plans/new_meal.html', context)
