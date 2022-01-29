from django.db import models

# Create your models here.
class Brand(models.Model):
    """
    this is Brand table
    """
    Name = models.CharField(max_length=100)
    Orgin = models.CharField(max_length=100 ,null=True)
    def __str__(self):
        return self.Name

class Products(models.Model):
    """
    this is Products tables
    """
    Name = models.CharField(max_length=100,null=True)
    Kind = models.CharField(max_length=100,null=True)
    Descreption = models.TextField(null=True)
    Expir_date = models.DateField(null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    #brand = models.ForeignKey(Brand,on_delete=models.CASCADE,max_digits=10, decimal_places=2,null=False)

    def __str__(self):
        return self.Name



