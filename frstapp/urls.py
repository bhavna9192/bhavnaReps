from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	# path('admin/', admin.site.urls),
	path('cronJob/', views.cronJob, name='cronJob'),
	path('testAction/',views.testAction),
	path('thanks/',views.thanks),
	path('modelForm/',views.modelForm),
	path('formsForm/',views.formsForm),
	path('studentData/',views.studentData),
	path('update/<int:id>/',views.update),
	path('delete/',views.delete),
	path('loginAuth/',views.loginAuth),
	path('logout/',views.logout),
	path('home/',views.home),
	# url(r'^home/',views.home), 
	url(r'^signup/$',views.signup, name='signup'),
	url(r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
	url(r'^register/$', views.register, name='register'),
	# path('celsius/', views.CelsiusView, name='celsius'),
	path('money/', views.money, name='money'),

]


