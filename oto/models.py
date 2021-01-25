from django.db import models

# Create your models here.

class Author_test(models.Model):
    name = models.CharField("作家姓名",max_length=10)

class Wife_test(models.Model):
    name = models.CharField("妻子姓名",max_length=10)
    author = models.OneToOneField(Author_test,on_delete=models.CASCADE)

