from django.db import models



# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_picture = models.ImageField(upload_to='product_picture/', null=True, blank=True)
    name = models.TextField(max_length=150, blank=False, null=False)
    color = models.TextField(max_length=150, blank=False, null=False)
    size = models.TextField(max_length=150, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)


    def __str__(self):
        return f"{self.name} - {self.color} - {self.size} - ${self.price}"




class Cart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

