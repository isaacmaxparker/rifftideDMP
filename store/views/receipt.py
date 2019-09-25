from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, orderId:str): 

   print("*****************************************")
   print(orderId)
   print("*****************************************")

   sale = cmod.Sale.objects.get(orderID=orderId)

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