from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, orderId:str): 

      
   cartID = request.session.get('cart_ID', 'NONE') 
   if cartID != 'NONE': 
       sale = cmod.Sale.objects.get(id=cartID)
   else:
       sale = cmod.Sale.objects.get(orderID=orderId)
    
   if sale.purchased == None:
      sale.finalize(orderId)
      del request.session['cart_ID']
      sale.save()

   saleItems = cmod.SaleItem.objects.filter(sale=sale, status ='A')

   context = {
       'total':sale.total,
       'subtotal':sale.subtotal,
       'tax':sale.tax,
       'saleItems':saleItems,
       'cart':sale,
       'sale':sale,
    }
   return request.dmp.render('receipt.html', context)