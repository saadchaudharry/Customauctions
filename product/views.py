from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from .models import Category,Products,contactus
from .forms import contact_form
from order.forms import order_all_form
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum

# MERCHANT_KEY="_BuGPdRFlxW%ZnF1"
MERCHANT_KEY="SG4UY9spY6dyf!l6"

# MERCHANT_KEY="eM7V7F3lj%zGP&Tr"


# import stripe
#
# stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.



class contactuss(CreateView):
    model = contactus
    form_class = contact_form
    template_name = 'contactUs.html'
    success_url = reverse_lazy('contactsss')

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

def product_list(request,category_slug):
    prod =Products.objects.filter(publish=True)
    if category_slug:
        catagory=get_object_or_404(Category,slug=category_slug)
        prod =prod.filter(category=catagory)
    context={'prod':prod}
    return render(request, 'prodlist.html', context)

def formjsjs(request):
    order_form =order_all_form(request.POST)
    if order_form.is_valid():
        instance =order_form.save(commit=True)
        instance.save()

    context={'order':instance,}

    return render(request,'hello.html',context)

def paytm(request):
    obj1 = request.POST.get('id')
    obj2 = request.POST.get('total')
    obj3 = request.POST.get('email')
    print(obj1,obj2,obj3)

    param_dict = {
        # 'MID': 'IziPPU18604609740449',
        'MID': 'ZdehqP52015247605360',
        'ORDER_ID': str(obj1),
        'TXN_AMOUNT':str(obj2),
        'CUST_ID': str(obj3),
        'INDUSTRY_TYPE_ID':'Retail',
        'PAYMENT_MODE_ONLY':'yes',
        'PAYMENT_TYPE_ID':['DC','CC'],
        'AUTH_MODE':'3D',
        'WEBSITE': 'DEFAULT',
        'CHANNEL_ID': 'WEB',
        # 'CALLBACK_URL': 'https://customauctions.in/handlerequest/',
        'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render(request, 'paytm.html', {'param_dict': param_dict})



@csrf_exempt
def handlerequest(request):
    form = request.POST
    checksum = None
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    if checksum is not None:
        verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
        if verify:
            if response_dict['RESPCODE'] == '01':
                print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})