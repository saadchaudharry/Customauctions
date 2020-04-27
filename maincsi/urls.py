"""maincsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import Category_list,product_list,product_detail,formjsjs,charge

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Category_list.as_view(),name="index"),
    path('1', formjsjs,name="indfdfex"),
    path('charge/',charge, name='charge'),
    path('p/<category_slug>', product_list,name="prod"),
    path('d/<slug:slug>', product_detail.as_view(),name="prod-det"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)