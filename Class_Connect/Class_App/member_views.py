from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Enrollment,Feedback,Query_Doubt

# from .models import Member


def registration(request):
    if request.method=="GET":
        return render(request, 'Class_app/student/student_registration.html')
    if request.method=="POST":
        stu_name=request.POST["name"]
        stu_email=request.POST["email"]
        stu_phone=request.POST["phone"]
        stu_city=request.POST["city"]
        stu_address=request.POST["address"]
        stu_choosecourse=request.POST["coursename"]
        stu_pic=request.FILES["studentPic"]
        student_obj=Enrollment(name=stu_name,email=stu_email,phone_no=stu_phone,city=stu_city,address=stu_address,choose_course=stu_choosecourse,fee_status=True,stu_pic=stu_pic)
        student_obj.save()
        messages.success(request,"❤️❤️ Registration Completed Successfully ❤️❤️")
        return redirect("student_registration")



def student_dashboard(request): 
    if "session_key" not in request.session.keys():
        return redirect("student_login")
    else:
        id=request.session["session_key"]
        stu_object=Enrollment.objects.get(student_id=id)
        context={"student_key":stu_object}
        return render(request,'Class_app/student/student_dashboard.html',context)


def logout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("student_login")


def student_login(request):
    if request.method == "GET":
        return render(request, 'Class_app/student/student_login.html')
    
    if request.method == "POST":
        stud_id = request.POST.get("ID")
        stud_password = request.POST.get("password")
        student_list = Enrollment.objects.filter(student_id=stud_id, password=stud_password, fee_status=True)
        print(student_list)
        
        if student_list.exists():
            student_obj = student_list.first()
            print(student_obj)
            request.session["session_key"] = stud_id
            request.session["role"] = "student"

            context = {
                "student_key": student_obj,
            }
            return render(request, 'Class_app/student/student_dashboard.html', context)
        else:
            messages.error(request, "Invalid User ID or YOUR FEE HAS NOT BEEN SUBMITTED")
            return redirect("student_login")

def feedback(request):
    if request.method=="GET":
        if "session_key" not in request.session.keys():
            return redirect ("student_login")
        else:
            return render(request, "Class_app/student/student_feedback.html")

    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_remark = request.POST.get("rating")
        user_review = request.POST.get("review")

        
        feedback_obj = Feedback(name=user_name, email=user_email, rating=user_remark, review=user_review)
        feedback_obj.save()

        messages.success(request, "Thank you for your valuable feedback! 👍👍")

        
        return redirect("feedback")

    # Render the feedback form template for GET requests


def reviews(request):
    feedbacks=Feedback.objects.all()
    return render(request,'Class_app/html/Reviews.html',{'feedbacks':feedbacks})

def querydoubt(request):

    if request.method =="GET":
        if "session_key" not in request.session.keys():
          return redirect ("student_login")
        else:
            return render(request, 'Class_app/student/query_doubt.html')
    

    if request.method =="POST":
        id=request.session["session_key"] 
        query_doubt=Query_Doubt(request.POST)
       
        if request.method == "POST":
            user_name=request.POST.get("name")
            user_email=request.POST.get("email")
            user_subject=request.POST.get("subject")
            user_question=request.POST.get("question")

            query_doubt_obj = Query_Doubt (name=user_name,email=user_email,subject=user_subject,Question=user_question)
            query_doubt_obj.save()
            messages.success(request, "your query has been submitted successfully 👍! 👍👍")
            return redirect(query_doubt)

# view Answer for doubts and query

def view_answer(request):
    if "session_key" not in request.session.keys():
        return redirect ("student_login")
    else:
         id=request.session["session_key"]
         answer_list= Query_Doubt.objects.filter(member_id=id)
         context={"answer_key":answer_list}

         return render(request,'Class_app/student/views_answer.html',context)