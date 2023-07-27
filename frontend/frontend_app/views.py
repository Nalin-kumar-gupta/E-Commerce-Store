from django.shortcuts import render

def index(request):
    return render(request, 'frontend_app/index.html')

def about(request):
    return render(request, 'frontend_app/about.html')

def shop(request):
    return render(request, 'frontend_app/product.html')

def cart(request):
    return render(request, 'frontend_app/shopping_cart.html')

def blog(request):
    return render(request, 'frontend_app/blog.html')

def contact(request):
    return render(request, 'frontend_app/contact.html')

def detail(request):
    return render(request, 'frontend_app/product-detail.html')
