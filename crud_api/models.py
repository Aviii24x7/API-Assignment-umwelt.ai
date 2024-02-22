from django.db import models

# Abstract models : For common fields
class CommonFieldsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        
        
# general models

class Category(CommonFieldsModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class Product(CommonFieldsModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Order(CommonFieldsModel):
    customer_name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)