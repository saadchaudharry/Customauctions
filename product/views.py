from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Category,Products

# Create your views here.


class Category_list(ListView):
    model = Category
    template_name ='catagory_list.html'


def product_list(request,category_slug):
    prod =Products.objects.filter(publish=True)
    if category_slug:
        catagory=get_object_or_404(Category,slug=category_slug)
        prod =prod.filter(category=catagory)
    context={'prod':prod}
    return render(request, 'prodlist.html', context)

