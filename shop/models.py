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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    design_file = models.FileField(upload_to='uploads/')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"
