from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Category, Product, ProductReview
from django.core.paginator import Paginator, EmptyPage


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    p = Paginator(products, 6)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'store/home.html', {'products': page})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    reviews = ProductReview.objects.filter(product=product)[:3]
    context = {
        'product': product, 'reviews': reviews
    }
    if request.method == 'GET':
        return render(request, 'store/product_detail.html', context)
    data = request.POST
    if not data.get('text'):
        context['error_message'] = "Please enter a review!!!"
        return render(request, 'store/product_detail.html', context)
    ProductReview.objects.create(text=data['text'], product=product, stars=data['stars'], user=request.user)
    return HttpResponseRedirect(reverse('store:product_detail', args=(product.slug,)))








