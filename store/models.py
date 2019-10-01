from django.db import models
from decimal import Decimal
from datetime import datetime

# Create your models here.
class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField(default='')


class Product(models.Model):

    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')
    isMain = models.BooleanField(default=False)
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    shirtColor = models.TextField(default="white")
    decor = models.TextField(default="white")
    cut = models.TextField(default ='')


    def image_url(self):

        image_url = 'https://storage.googleapis.com/rifftidesite-content/static/store/media/samples/' + self.name + ' - ' + self.shirtColor

        if self.decor != "":
            image_url = image_url + ' ' + self.decor
        if self.cut != "":
            image_url = image_url + ' ' + self.cut

        image_url = image_url + ".png"

        return image_url


    def images_url(self):
        urls = []
        for pi in ProductImage.objects.filter(product=self):
            urls.append(pi.image_url())
        # if list is empty append no iimage available
        if len(urls) == 0:
            urls.append('/static/catalog/media/products/noimage.png')
        return urls

class ProductImage(models.Model):
    'an image for a product'
    filename = models.TextField(default='noimage.png')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    
    def image_url(self):
        return '/static/store/media/samples/' + self.filename + ' teal' + '.png'

TAX_RATE = Decimal(".00")

class Sale(models.Model):
        #user = models.ForeignKey("account.User", on_delete=models.PROTECT)
        created = models.DateTimeField(auto_now_add=True)
        purchased = models.DateTimeField(null=True, default=None)
        subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe
        shipMethod = models.TextField(null=True,default=None)
        referrer = models.TextField(null=True, default=None)
        orderID = models.TextField(null=True, default=None)

        def recalculate(self):
            sales = SaleItem.objects.filter(sale=self, status='A')
            sub = Decimal("0.0")
            for sale in sales:
                sub += sale.price
            self.subtotal = sub
            if self.shipMethod != "IP":
                self.total = self.tax = 5
            else:
                self.tax = 0
            self.total = round(self.subtotal + self.tax,2)
            self.save()

        def finalize(self,orderId):
            '''Finalizes the sale'''
            self.orderID = orderId
            if self.purchased is not None:
                raise ValueError("This sale has already been finalized")

            self.purchased = datetime.now()

class SaleItem(models.Model):
        STATUS_CHOICES = [
            ( 'A', 'Active' ),
            ( 'D', 'Deleted' ),
        ]
        status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
        sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
        product = models.ForeignKey("Product", on_delete=models.PROTECT)
        quantity = models.IntegerField(default=0)
        size = models.TextField(null=True)
        price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        class Meta:
            ordering = [ 'product__name' ]