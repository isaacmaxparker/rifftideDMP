from django.db import models

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

        image_url = '/static/store/media/samples/' + self.name + ' - ' + self.shirtColor

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