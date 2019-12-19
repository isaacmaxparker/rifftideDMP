from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from store import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request): 

   sales=cmod.Sale.objects.all().exclude(orderID=None).order_by('purchased')

   pSales = sales.filter(status='P')
   oSales = sales.filter(status='O')
   rSales = sales.filter(status='R')
   dSales = sales.filter(status='D')

   context = {
       'sales':sales,
       'pSales':pSales,
       'oSales':oSales,
       'rSales':rSales,
       'dSales':dSales,
    }
   return request.dmp.render('orders.html', context)


@view_function
def update(request, sale:cmod.Sale):
   status=sale.status
   newsale = cmod.Sale.objects.get(id=sale.id)
   
   if status == 'P':
      newsale.status = 'O'
   elif status == 'O':
      newsale.status = 'R'
   elif status == 'I':
      newsale.status = 'P'
   elif status == 'R':
      newsale.status = 'D'
   newsale.save()

   newersale = cmod.Sale.objects.get(id=newsale.id)
   return HttpResponseRedirect('/account/orders')

@view_function
def downdate(request, sale:cmod.Sale):
   status=sale.status
   newsale = cmod.Sale.objects.get(id=sale.id)
   
   if status == 'O':
      newsale.status = 'P'
   elif status == 'R':
      newsale.status = 'O'
   elif status == 'P':
      newsale.status = 'I'
   elif status == 'D':
      newsale.status = 'R'
   newsale.save()

   newersale = cmod.Sale.objects.get(id=newsale.id)
   return HttpResponseRedirect('/account/orders')

@view_function
def delete(request, sale:cmod.Sale):
   status=sale.status
   newsale = cmod.Sale.objects.get(id=sale.id)
   
   newsale.status='E'
   newsale.save()

   newersale = cmod.Sale.objects.get(id=newsale.id)
   return HttpResponseRedirect('/account/orders')