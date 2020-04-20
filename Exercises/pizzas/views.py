from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

def index(request):
    """The home page for Pizzaria."""
    return render(request, 'pizzas/index.html')

@login_required
def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    """Show a single pizza and all its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

@login_required
def new_pizza(request):
    """Add a new pizza."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PizzaForm
    else:
        # POST data submitted; process data.
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            return redirect('pizzas:pizzas')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)

@login_required
def new_topping(request, pizza_id):
    """Add a new topping for a pizza."""
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ToppingForm()
    else:
        # POST data submitted; process data.
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    # Display a blank or invalid form.
    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/new_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    """Edit an existing topping."""
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        # Initial request; pre-fill form with current topping.
        form = ToppingForm(instance=topping)
    else:
        # POST data submitted; process data.
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza.id)
    context = {'topping': topping, 'pizza': pizza, 'form': form}
    return render(request, 'pizzas/edit_topping.html', context)
