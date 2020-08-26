from django.db import models

# Create your models here.

class UserModel(models.Model):
    usernum = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phno = models.IntegerField(unique=True)
    password = models.CharField(max_length=40)

class ProductModel(models.Model):
    ptype = models.CharField(max_length=40)
    pname = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2,max_digits=9,default=0)
    descriptionproduct = models.TextField()
    image = models.ImageField(upload_to='products/')
    userid = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=0)

class ProductMessage(models.Model):
    customermsg = models.TextField(null=True)
    customerreply = models.TextField(null=True)
    productid = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    fromid = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    toid = models.IntegerField()