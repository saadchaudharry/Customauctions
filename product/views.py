from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Category,Products
from order.forms import order_all_form
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.


class Category_list(ListView):
    model = Category
    template_name ='catagory_list.html'


class product_detail(DetailView):
    model = Products
    template_name = 'product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(product_detail, self).get_context_data(*args, **kwargs)
        context['form'] = order_all_form
        return context


def formjsjs(request):
    order_form =order_all_form(request.POST)
    key       =settings.STRIPE_PUBLISHABLE_KEY
    if order_form.is_valid():
        instance =order_form.save(commit=True)
        instance.save()

    context={'form':order_form,'order':instance,'key':key}

    return render(request,'hello.html',context)

#
# @app.route('/checkout')
# def checkout(request):
#   intent = # ... Fetch or create the PaymentIntent
#   return render(request,'checkout.html', {'client_secret'=intent.client_secret})


def charge(request): # new
    if request.method == 'POST':
        amount=request.POST.get('order')
        orderid=request.POST.get('ids')
        b=int(amount)*100
        print(type(b))
        charge = stripe.Charge.create(
            amount=b,
            currency="inr",
            description=str(orderid),
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')

def product_list(request,category_slug):
    prod =Products.objects.filter(publish=True)
    if category_slug:
        catagory=get_object_or_404(Category,slug=category_slug)
        prod =prod.filter(category=catagory)
    context={'prod':prod}
    return render(request, 'prodlist.html', context)

