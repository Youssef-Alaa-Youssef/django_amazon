from django.db import models
from catetegory.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    image =models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name='category_posts')

    def __str__(self):
        return self.name

