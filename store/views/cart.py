from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request): 

    cartID = request.session.get('cart_ID', 'NONE') 
    print("***************************************AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
    print(cartID)
    if cartID != 'NONE':
        sale = cmod.Sale.objects.get(id=cartID)
        sale.recalculate()
        saleItems = cmod.SaleItem.objects.filter(sale=sale, status = 'A')
    else:
        print("ASFDSAwagnxsaergcmdswqtvfde$wq@#hmvdretw$tfgb<ge$#erthbnm")
        sale = cmod.Sale()
        saleItems = cmod.SaleItem.objects.filter(sale=sale, status = 'A')
    print(sale)
    print(saleItems[0])

    context = {
       'total':sale.total,
       'subtotal':sale.subtotal,
       'tax':sale.tax,
       'saleItems':saleItems,
       'cart':sale,
    }
    return request.dmp.render('cart.html', context)

@view_function
def remove(request, product:cmod.Product):
    cartID = request.session.get('cart_ID', 'NONE') 
    if cartID != 'NONE':
        sale = cmod.Sale.objects.get(id=cartID)
    saleItem = cmod.SaleItem.objects.get(sale=sale, product=product)
    saleItem.status = 'D'
    saleItem.save()
    return HttpResponseRedirect('/store/cart/')