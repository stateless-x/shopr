# Django's ORM
from django.contrib.auth.models import User
from django.db import models

# defining new model
class Category(models.Model):
    name = models.CharField(max_length=255)
    # config the model under this class
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    # use this line to make it show names of categories instead of generic name like Category Object(1)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE);
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    