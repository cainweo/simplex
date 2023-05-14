from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html') 

def staff(request):
    return render(request, 'dashboard/staff.html ')

def products(request):
    items = Product.objects.all() # using ORM shorter than usual sql code
    #items = Product.objects.raw('SELECT * FROM dashboard_product')

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form'  : form,

    }
    return render(request, 'dashboard/products.html', context)  

def products_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-products')
    return render(request, 'dashboard/products_delete.html')


def products_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=item )
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,

    }
    return render(request, 'dashboard/products_update.html', context)

def orders(request):
    return render(request, 'dashboard/orders.html ')      