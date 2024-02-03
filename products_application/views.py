from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def get_all_products_screen(request): 
  # Product(name='product 1', quantity=30, price=19.99, description='some description for product 1').save()
  # Product(name='product 2', quantity=50, price=29.99, description='some description for product 2').save()
  products = Product.objects.all()
  return render(request, 'get-all-products-screen.html', { 'products': products })

def get_single_product_detail_screen(request, id): 
  product = Product.objects.get(pk=id)
  return render(request, 'get-single-product-details-screen.html', { 'product': product })


def add_product_screen(request):
  if request.method == 'GET':
    form = ProductForm()
    return render(request, 'add-product-screen.html', { 'form': form })

  form = ProductForm(request.POST, request.FILES)
  if form.is_valid():
    product = form.save()
    return redirect('products_application:product_details_screen', id=product.id) 
   

def edit_product_screen(request, id):
  product = get_object_or_404(Product, pk=id)
  if request.method == 'GET':
    form = ProductForm(instance=product)
    return render(request, 'edit-product-screen.html', { 'form': form })
  
  form = ProductForm(request.POST, request.FILES, instance=product)
  if form.is_valid():
    product = form.save()
    return redirect('products_application:product_details_screen', id=product.id) 
    

@require_POST
def delete_product_action(request, id):
  product = get_object_or_404(Product, pk=id) 
  if 'confirm_delete' in request.POST:
    product.delete()
    return redirect('products_application:products_list_screen')  
