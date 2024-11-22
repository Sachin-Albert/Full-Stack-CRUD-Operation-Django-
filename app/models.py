from django.db import models

class createdata(models.Model):
    name = models.CharField(max_length=200,null=False)
    phone = models.IntegerField()
    para = models.TextField(max_length=5000)

    def __str__(self):
        return self.name
    
class Register(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200)

    def __str__(self):
        return self.name