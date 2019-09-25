from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings

@view_function
def process_request(request): 

    shippingMethod = " "
    shippingPerson = " "

    cartID = request.session.get('cart_ID', 'NONE') 

    if request.method == 'POST': 
        shippingMethod = str(request.POST['shipSelect'])
        shippingPerson = str(request.POST['personSelect'])
    else:
        if cartID != 'NONE':
            sale = cmod.Sale.objects.get(id=cartID)
            shippingMethod = sale.shipMethod
            shippingPerson = sale.referrer



    if cartID != 'NONE':
        sale = cmod.Sale.objects.get(id=cartID)
        sale.recalculate()
        saleItems = cmod.SaleItem.objects.filter(sale=sale, status = 'A')

    else:
        sale = cmod.Sale()
        saleItems = cmod.SaleItem.objects.filter(sale=sale, status = 'A')

    if shippingMethod == "IP":
        sale.shipMethod = shippingMethod
        sale.referrer = shippingPerson
    else:
        sale.shipMethod = shippingMethod

    sale.recalculate()

    context = {
       'total':sale.total,
       'subtotal':sale.subtotal,
       'tax':sale.tax,
       'saleItems':saleItems,
       'cart':sale,
       'SBClientId':settings.SBCLIENTID,
       'shipSelect':shippingMethod,
       'personSelect':shippingPerson,
    }
    return request.dmp.render('cart.html', context)

    

@view_function
def remove(request, saleItem:cmod.SaleItem):
    cartID = request.session.get('cart_ID', 'NONE') 
    saleItem = cmod.SaleItem.objects.get(id=saleItem.id)
    saleItem.status = 'D'
    saleItem.save()
    return HttpResponseRedirect('/store/cart/')

@view_function
def finishSale(request,orderId:str):
    cartID = request.session.get('cart_ID', 'NONE') 
    sale = cmod.Sale.objects.get(id=cartID)
    print("*********************************** Things")
    print(orderId)
    sale.finalize(orderId)
    del request.session['cart_ID']
    print(request.session.get('cart_ID'))
    sale.save()
    data = {'orderId':orderId}
    return HttpResponseRedirect('/store/receipt/'+orderId)
    