from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, product:cmod.Product):

    variations = cmod.Product.objects.filter(name=product.name,cut=product.cut)

    if request.method == 'POST': 
        
        quantwant = int(request.POST['QuantOrd'])

        if quantwant == 0:
            context = {
                'name':product.name,
                'price':product.price,
                'shirtColor':product.shirtColor,
                'decorColor':product.decor,
                'desc':product.description,
                'imageurl':product.image_url(),
                'variations':variations,
                'message':'Quantity can\'t be zero'
            }
            return request.dmp.render('product.html', context)

        size = str(request.POST['shirtSize'])
        
        cartID = request.session.get('cart_ID', 'None')
        if (cartID == 'None'):
            sale = cmod.Sale()
        else:
            sale = cmod.Sale.objects.get(id=cartID)

        sale.save()
    
        sale2 = cmod.Sale.objects.get(id=sale.id)

        request.session['cart_ID'] = sale2.id

        try:
            thisItem = cmod.SaleItem.objects.get(sale=sale2, product=product)
            thisItem.quantity = saleItem.quantity + quantwant
            thisItem.save()
        except:
            thisItem = cmod.SaleItem()
            thisItem.sale = sale
            thisItem.product = product
            thisItem.quantity = quantwant
            thisItem.size = size
            thisItem.price = round(product.price * thisItem.quantity,2)
            thisItem.save()
        
        return HttpResponseRedirect('/store')




    context = {    
        'name':product.name,
        'price':product.price,
        'shirtColor':product.shirtColor,
        'decorColor':product.decor,
        'desc':product.description,
        'imageurl':product.image_url(),
        'variations':variations,
        'message':'',
    }
    return request.dmp.render('product.html', context)

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product':product
    })
