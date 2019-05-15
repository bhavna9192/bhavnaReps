from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import Employee,Place,Restaurant,Waiter 
from django.http import HttpResponse
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

def oneToOne(request):
	# create place 
	# p1 = Place(name='Demon Dogs', address='944 W. Fullerton')	
	p1=Place.objects.create(name='Demon Dogs', address='944 W. Fullerton')
	p1.save()
	print("p1=",p1)
	p2 = Place(name='Ace Hardware', address='1013 N. Ashland')
	p2.save()   
	print("p2=",p2.address)  

	# create restaurent
	r= Restaurant.objects.create(place=p1,serves_hot_dogs=True,owner="bhavna",serves_pizza=False)
	print("r=",r.place.name,r.owner)
	r2=Restaurant.objects.filter(place_id=10).first()	
	print("r2=======",r2)
		
	w=Waiter(restaurant=r2,name="abc")
	w.save()
	print("waiter=",w)

	

	return  HttpResponse('one to one user, hello!') 


	# class Place(models.Model):
	# 	name = models.CharField(max_length=50)
	# 	address = models.CharField(max_length=80)

	# 	# On Python 3:	 def __str__(self):
	# 	def __str__(self):
	# 	    return u"%s the place" % self.name

	# class Restaurant(models.Model):
	#     place = models.OneToOneField(Place, primary_key=True,on_delete=models.CASCADE)
	#     serves_hot_dogs = models.BooleanField()
	#     serves_pizza = models.BooleanField()

	#     # On Python 3: def __str__(self):
	#     def __str__(self):
	#         return u"%s the restaurant" % self.place.name

	# class Waiter(models.Model):	
	 #    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	 #    name = models.CharField(max_length=50)

	 #    # On Python 3: def __str__(self):
	 #    def __str__(self):
	 #    	return u"%s the waiter at %s" % (self.name, self.restaurant)
	 

