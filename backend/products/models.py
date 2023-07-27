from django.db import models

class Category(models.Model):
    TYPES = (
        ('electronics', 'electronics'),
        ('jewelery', 'jewelery'),
        ("men's clothing", "men's clothing"),
        ("women's clothing", "women's clothing"),
    )
    type = models.CharField(max_length=30, choices=TYPES, default="women's clothing")

   

    

    def __str__(self):
        return f"{self.get_gender_display()} - {self.get_colors_display()}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(default="https://images.unsplash.com/random/?girlshirt")
    brand = models.CharField(max_length=50, default='LocalBrand')
    stock = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return self.name
