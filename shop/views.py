from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm

# ✅ Home page view
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import OrderForm

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return render(request, 'shop/success.html')
    else:
        form = OrderForm()

    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})
