from django.shortcuts import render
from product.models import Category, Product

# Create your views here.
def main_view(request):
    if request.method=='GET':
        categories = Category.objects.all()
        products = Product.objects.all()
        return render(request, 'main.html', {'categories':categories, 'products':products})