from django.db import models

class category(models.Model):
    name=models.CharField(max_length=20)
    describtion=models.TextField()

    def __str__(self) :
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=20)
    describtion=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField()
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.name