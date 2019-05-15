from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from apscheduler.scheduler import Scheduler
from .forms import NameForm,StudentForm,ContactForm,updateForm,loginForm
from django.views.decorators.csrf import csrf_exempt
from .models import userDetail,Student,ContactModel
from django.contrib import messages

# signin////////////

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView


@csrf_exempt
def home(request):
    return render(request, 'home.html')     

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# signout////////////

 
@csrf_exempt
def cronJob(request):       
    a=request.POST.get('inp1')  


    # data=User.objects.all() 
    # for newdata in data:
    #   print(newdata.username)     

    # sched = Scheduler()
    # sched.start()

    # def some_job():
    #     print("Every 10 seconds") 

    # sched.add_interval_job(some_job, seconds = 10)
    return HttpResponse('Hello, welcome to the index page.')

@csrf_exempt
def loginAuth(request): 
    if request.method == 'POST':  
        form=loginForm(request.POST)
        return HttpResponse("success")

    else:  
        form=loginForm()
        return render(request,'loginAuth.html',{'form':form})

@csrf_exempt
def logout(request): 
   
    return HttpResponse('Hello, welcome to the home page.')

   


@csrf_exempt
def testAction(request):
    if request.method == 'POST':        
        a=request.POST.get('inp4')    
        
        form = NameForm(request.POST)
       
        if form.is_valid():
            print("inside formvalid post")
            
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print("inside get")

    return render(request,'actionUrl.html',{'current_name':"Bhavna",'form': form})

@csrf_exempt
def thanks(request):
    return HttpResponse('Hello, welcome to the thanks page.')

@csrf_exempt
def modelForm(request):
    if request.method == 'POST':      
            
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Error")
    else:
        form = StudentForm()
    return render(request, 'modelForm.html', {'form': form})

@csrf_exempt
def formsForm(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')           
            ContactModel.objects.create(name=name,message=message,email=email)
            # form.save()



            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()  
    
    return render(request, 'formsForm.html', {'form': form})

    
@csrf_exempt
def studentData(request):

    studentdata=Student.objects.all()
    
    return render(request, 'crud.html', {'studentdata': studentdata})

@csrf_exempt
def update(request,id):     
    if request.method == 'POST': 
        id_student=request.POST.get('id_student')
        flag=request.POST.get('flag')           
        
        if flag=='false':                                 
            studentdata=Student.objects.filter(id=id_student).update(name=request.POST["firstname"],
                last_name=request.POST["lastname"],age=request.POST["age"],email=request.POST["email"])                  
            return HttpResponse("success")
        else:
            return HttpResponse("fail")                  
            

    else:       
        data=Student.objects.filter(id=id)
        return render(request, 'update.html',{'data':data})

@csrf_exempt
def delete(request):
    if request.method == 'POST': 
        id_student=request.POST.get('id_student')
        flag=request.POST.get('flag')
        if flag=='true':
            print("id_student=",id_student,flag)
            Student.objects.filter(id=id_student).delete()  
                  
            return HttpResponse("success") 

    else:
        studentdata=Student.objects.all()
        return render(request, 'crud.html')        
        
    
   
@csrf_exempt
def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
 
    else:
        f = UserCreationForm()
 
    return render(request, 'register.html', {'form': f})



# class CelsiusView():
#     print('1111')
#     def __init__(self, temperature = 0):
#         print('temp=',temperature)
#         self.set_temperature(temperature)

#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32

#     # new update
#     def get_temperature(self):
#         return self._temperature

#     def set_temperature(self, value):
#         print('value==',value)
#         # if value < 0:
#         #     raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value

class Money:
    def __init__(self, dollars, cents):         
        self.name='abc'
        self.total_cents = dollars * 100 + cents

    # Getter and setter for dollars...

    @property
    def dollars(self):
        print('dollar=',self.total_cents // 100)
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    # And the getter and setter for cents.
    @property
    def cents(self):
        print('cents=',self.total_cents % 100)
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents

def money(request): 

    money = Money(3, 10)
    print("I have {} dollar and {} cents.".format(money.dollars, money.cents))   

    # my_tuple = ()    
    # my_tuple = (1, 2, 3,[4,3,2,'abc',1])

    # print("tuple before sorting=",my_tuple)
    # lastList = my_tuple[3]

    # lastList.sort(key=lambda v: (isinstance(v, str), v))

    # my_tuple = my_tuple[:-1] + (lastList,)
    # print('my_tuple after sorted =',my_tuple)

    return HttpResponse('success')



