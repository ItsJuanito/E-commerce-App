from django.shortcuts import render

from apps.product.models import Product

# Create your views here.
def homepage(request):
    newest_products = Product.objects.all()[0:8]
    
    return render(request, 'core/homepage.html', { 'newest_products' : newest_products })

def contact(request):
    return render(request, 'core/contact.html')