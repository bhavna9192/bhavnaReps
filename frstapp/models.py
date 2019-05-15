from django.db import models


class userDetail(models.Model):	
	name = models.TextField()	

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40,null=True, blank=True) 
    last_name =models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254)    

    def __str__(self):
        return self.name+" "+self.last_name

class ContactModel(models.Model):
    name = models.CharField(max_length=30,null=True, blank=True)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=2000) 

class loginModel(models.Model):   
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=40,null=True, blank=True) 

    def __str__(self):
        return self.email


class registerModel(models.Model):
    name=models.CharField(max_length=40,null=True, blank=True)
    email= models.EmailField(max_length=254)
    password=models.CharField(max_length=40 ,blank=True)
    age=models.IntegerField(null=True, blank=True)




        



    """docstring for ClassName"""
    # def __init__(self, arg):
    #    	super(ContactModel, self).__init__()
    # 	self.arg = arg
		        

    

