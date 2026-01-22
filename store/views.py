from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product

from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return user.is_superuser


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
@user_passes_test(admin_required)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()    
    return render(request, 'store/product_form.html', {'form': form})

@login_required
@user_passes_test(admin_required)
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'store/product_form.html', {'form': form})


@login_required
@user_passes_test(admin_required)
def product_delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect('product_list')