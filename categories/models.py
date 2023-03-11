from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100)
    describtion=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='photos/%m/%y/%d')
    activate=models.BooleanField(default=True)
        
   
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()
    
    
    @classmethod
    def get_category(cls,id):
        try:
            category = cls.objects.get(pk=id)
            return category
        except Exception as e:
            return None