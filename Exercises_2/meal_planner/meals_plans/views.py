from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Day, Meal
from .forms import MealForm

def index(request):
    """The home page for Meal Plans."""
    return render(request, 'meals_plans/index.html')

@login_required
def days(request):
    """Show all days."""
    days = Day.objects.order_by('date_added')
    context = {'days': days}
    return render(request, 'meals_plans/days.html', context)

@login_required
def day(request, day_id):
    """Show a single topic and all its entries."""
    day = Day.objects.get(id=day_id)
    meals = day.meal_set.order_by('-date_added')
    context = {'day': day, 'meals': meals}
    return render(request, 'meals_plans/day.html', context)

@login_required
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

@login_required
def edit_meal(request, meal_id):
    """Edit an existing meal."""
    meal = Meal.objects.get(id=meal_id)
    day = meal.day

    if request.method != 'POST':
        # Initial request; pre-fill form with current meal.
        form = MealForm(instance=meal)
    else:
        # POST data submitted; process data.
        form = MealForm(instance=meal, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals_plans:day', day_id=day.id)

    context = {'meal': meal, 'day': day, 'form': form}
    return render(request, 'meals_plans/edit_meal.html', context)
