from django.shortcuts import render, redirect
from .models import PizzaOrder
from .forms import PizzaOrderForm

# View to handle order placement
def order_pizza(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Redirect to order list after form submission
    else:
        form = PizzaOrderForm()  # Display an empty form if it's a GET request
    return render(request, 'orders/order_form.html', {'form': form})

# View to display all orders
def order_list(request):
    orders = PizzaOrder.objects.all()  # Fetch all pizza orders
    return render(request, 'orders/order_list.html', {'orders': orders})

# Redirect root `/` to the order form
def redirect_to_order_form(request):
    return redirect('order_pizza')  # Redirect root to order form

