from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("course/<int:course_id>/", views.course_details, name="course_details"),
    path("exam/<int:question_id>/submit/", views.submit, name="submit"),
    path("exam/result/<int:submission_id>/", views.show_exam_result, name="show_exam_result"),
]
