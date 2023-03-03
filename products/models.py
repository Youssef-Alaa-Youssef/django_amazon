from django.db import models

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
class Product(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    image =models.ImageField(upload_to='images/', null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

