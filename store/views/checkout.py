from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect
from store import models as cmod
from django.conf import settings

@view_function
def process_request(request, sale:cmod.Sale):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        CheckoutForm.sale = sale
        # Check if the form is valid:
        if form.is_valid():
            for items in cmod.SaleItem.objects.filter(sale=sale, status='A'):
                items.product.quantity = items.product.quantity - items.quantity
                items.product.save()

            id = sale.id   
            return HttpResponseRedirect('/store/receipt/' + str(id))

           # return request.dmp.render('/account/templates/checkout.html')

    # If this is a GET (or any other method) create the default form.
    else:
        form = CheckoutForm()
    return request.dmp.render('checkout.html', {
        'form': form,
        'SBClientId':settings.SBCLIENTID,
        'total':sale.total,
    })





class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address')
    city = forms.CharField(label='Shipping City')
    state = forms.CharField(label='Shipping State')
    zipcode = forms.CharField(label='Shipping Zip Code')
    stripeToken = forms.CharField(widget=forms.HiddenInput)
    
    def clean(self):       
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))