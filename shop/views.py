from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm

# ✅ Home page view
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

# ✅ Product detail + order form
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return render(request, 'shop/success.html')
    else:
        form = OrderForm()

    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})
