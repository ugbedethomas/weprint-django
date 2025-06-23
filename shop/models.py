from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('business_cards', 'Business Cards'),
        ('flyers', 'Flyers'),
        ('stickers', 'Stickers'),
        ('mugs', 'Mugs'),
        ('tshirts', 'T-Shirts')
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField()
    quantity = models.IntegerField(default=1)
    from django.utils import timezone

    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"

