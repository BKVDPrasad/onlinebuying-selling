from django.db import models

#Admin can manage everything this site

class UserModel(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    contactno = models.IntegerField()
    password = models.CharField(max_length=30)

class ProductModel(models.Model):
    userid = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=0)
    pno = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField(null=True)
    photo =models.ImageField(upload_to='media/products/',null=True)


class ReportModel(models.Model):
    uid = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    logintime = models.DateTimeField()
    logouttime = models.DateTimeField()

class QuestionModel(models.Model):
    uid = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    qid = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=30)
    ans = models.TextField()
