from django.shortcuts import render
from store.models import Product
from django.core.paginator import Paginator

# Create your views here.
def store(request):
    products = None

    products = Product.objects.all().filter(is_available=True)
    # paginator = Paginator(products, 6)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # page_count = products.count()

    context = {
        'products': products,
        # 'page_count': page_count
    }

    return render(request, 'store/store.html', context)
