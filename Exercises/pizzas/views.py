from django.shortcuts import render, redirect

from .models import Pizza
from .forms import PizzaForm, ToppingForm

def index(request):
    """The home page for Pizzaria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza and all its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

def new_pizza(request):
    """Add a new pizza."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PizzaForm
    else:
        # POST data submitted; process data.
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizzas')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)

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
