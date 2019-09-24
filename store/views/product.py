from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponse

@view_function
def process_request(request, product:cmod.Product):

    variations = cmod.Product.objects.filter(name=product.name,cut=product.cut)

    context = {    
        'name':product.name,
        'price':product.price,
        'shirtColor':product.shirtColor,
        'decorColor':product.decor,
        'desc':product.description,
        'imageurl':product.image_url(),
        'variations':variations
    }
    return request.dmp.render('product.html', context)

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product':product
    })
