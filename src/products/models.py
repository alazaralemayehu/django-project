from django.db import models
import random,os
from django.urls import reverse

def uplaod_image_path(instance, filename):
  new_filename = random.randint(1,10000000)
  base_name = os.path.basename(filename)
  name, ext = os.path.splitext(base_name)
  final_filename = f'{new_filename}{ext}'
  return f'products/{final_filename}'

class ProductManager(models.Manager):
  def get_by_id(self, id):
    qs =  self.get_queryset().filter(id=id)
    if qs.count() ==1:
      return qs.first()
    return None

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=20, default= 20.00)
  image = models.ImageField(upload_to=uplaod_image_path, null=True, blank=True)
  slug = models.SlugField(default='uncategorized')
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = ProductManager()

  def get_absolute_url(self):
    return reverse("products:detail", kwargs={"pk":self.pk})
    # return "/products/{pk}/".format(pk=self.pk)

  def __str__(self):
    return self.title

 