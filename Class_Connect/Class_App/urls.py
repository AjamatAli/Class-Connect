from django.urls import path
from .import views,member_views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),  
    path("course/", views.course, name="course"),
    path("student_registration/", member_views.registration, name="student_registration"),
    path("student_login/", member_views.student_login, name="student_login"),
    path("dashboard/", member_views.student_dashboard, name="student_dashboard"),
    path("feedback/", member_views.feedback, name="feedback"),
    path("logout/", member_views.logout, name="logout"),
    path("reviews/", member_views.reviews, name="logout"),
    path('querydobut/',member_views.querydoubt, name='querydoubt'),
    path('view_answer/', member_views.view_answer, name='view_answer'),


]


