from django.db import models
from categories.models import Category
from django.shortcuts import reverse, get_object_or_404

# Create your models here.

class NewProducts(models.Model):
    id=models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name=  'ID')
    name= models.CharField(max_length=100)
    describtion=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='photos/%m/%y/%d')
    activate=models.BooleanField(default=True)
    categories=models.ForeignKey(Category,on_delete=models.CASCADE, null=True,
                                 related_name='category_posts')
    # price=models.IntegerField(max_value=6,label='price',initial='price')

      
    def __str__(self):
        return self.name
    
    
    
    def get_show_url(self):
        return reverse('show', args={self.id})