from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'Class_app/html/index.html')

def about(request):
    return render(request,'Class_app/html/About_Us.html')


def contact(request):

    if request.method=="POST":#http protocol sends user data using POST method
         user_name=request.POST["name"]#request.POST[]built-in dictionary 
         user_email  =request.POST["email"]
         user_question=request.POST["question"]
         #print(user_name,user_email,,user_question)
         contact_obj=Contact(name=user_name,email=user_email,Question=user_question)#creating Contact class object
         contact_obj.save()#ORM map with contact table fields
         messages.success(request,"❤❤❤Thanku for contacting us We will reach you soon❤❤❤")
    
         return redirect("contact")#it is logical name of the view 
    return render(request,'class_app/html/contact.html')

def course(request):
    return render(request,'Class_app/html/course.html')


