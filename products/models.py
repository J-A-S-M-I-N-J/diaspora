from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    """A model to create a category for the products"""
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """A model to create a product"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_inventory(self):
        return self.inventory.quantity

class Inventory(models.Model):
    """A model to create a product inventory"""
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.product.name

@receiver(post_save, sender=Product)
def create_or_update_inventory(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Inventory.objects.create(product=instance)
    # Existing users: just save the profile
    instance.Inventory.save()