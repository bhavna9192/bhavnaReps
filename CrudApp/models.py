from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):        
        return "name: {0}, address: {1}".format(self.name, self.address)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True,on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()
    owner=models.CharField(max_length=50,null=True,blank=True)

    # On Python 3: def __str__(self):
    # def __str__(self):
    #     return u"%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    # On Python 3: def __str__(self):
    def __str__(self):
    	return u"%s the waiter at %s" % (self.name, self.restaurant)
 