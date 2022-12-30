from django.shortcuts import render
from store.models import Product
from category.models import Category


def home(request):
    products = None
    categories = None
    name = 'Bedroom'
    number = 0

    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all().filter(is_display=True)
    
    number = products.filter(category__category_name=name).count()
    # paginator = Paginator(products, 6)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # page_count = products.count()

    context = {
        'products': products,
        'categories': categories,
        'number': number,
        'name': name,
        # 'page_count': page_count
    }

    return render(request, 'home.html', context)
