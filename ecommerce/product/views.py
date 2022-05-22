from django.shortcuts import render
from .models import category,Product
from cart.forms import CartAddProductForm
# Create your views here.
def m(request):
    categories= category.objects.all()
    products= Product.objects.all().order_by('-id')
    return render (request , 'pages/home.html',
    {"allproducts":products,"allcategories":categories})


def Category(request,categoryid):
    categories= category.objects.all()
    mycatygory= category.objects.get(id=categoryid)
    products= Product.objects.all().order_by('-id').filter(category_id = categoryid)
    return render (request , 'pages/home.html',
    {"allproducts":products,"allcategories":categories})


def product(request,productid):
    categories= category.objects.all()
    myproduct= Product.objects.get(id=productid)
    cart_product_form = CartAddProductForm()
    return render (request , 'pages/product-detail.html',
    {"myproduct":myproduct,"allcategories":categories,'cart_product_form':cart_product_form})


def Cart(request):
    categories= category.objects.all()
    myproduct= Product.objects.all()
    return render (request , 'pages/cart.html',
    {"myproduct":myproduct,"allcategories":categories})
