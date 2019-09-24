from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from math import ceil

ITEMS_PAGE_PAGE = 8


@view_function
def process_request(request, page:int=1, cat:int=0,color:int=0):
  
    if cat !=0:
        category = cmod.Category.objects.get(id=cat)
    else:
        category = None
    products = cmod.Product.objects.filter(status="A")
    catid=0

    if category is not None:
        products = products.filter(category=category)
        if cat == 1:
            products = products.filter(cut='')
        if cat == 2:
            products = products.filter(cut='womens')
        catid=category.id
    
    if color != 0:
        if color == 1:
            products = products.filter(shirtColor='black')
        if color == 2:
            products = products.filter(shirtColor='white')
        if color == 3:
            products = products.filter(shirtColor='teal')
        if color == 4:
            products = products.filter(shirtColor='grey')
    else:
        products = products.filter(isMain=True)       

    if color == 0 and category is None:
        filtered = False
    else:
        filtered = True

    pgproducts= products[(page - 1) * ITEMS_PAGE_PAGE: page * ITEMS_PAGE_PAGE]
    context = {
        'category':category,
        'catid':catid,
        'colorid':color,
        'filtered':filtered,
        'products':pgproducts,
        'page':page,
        'numpages': ceil(products.count() / ITEMS_PAGE_PAGE),
       
    }
    return request.dmp.render('index.html', context)
