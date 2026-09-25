from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Course, Question, Choice, Submission, Learner


def home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {"courses": courses})


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "course_details_bootstrap.html", {"course": course})


def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method != "POST":
        return redirect("course_details", course_id=question.course_id)

    selected_id = request.POST.get("choice")
    selected = Choice.objects.filter(pk=selected_id, question=question).first()

    user = request.user
    if not user.is_authenticated:
        user, _ = User.objects.get_or_create(username="demo_learner")
        learner, _ = Learner.objects.get_or_create(user=user)
    else:
        learner, _ = Learner.objects.get_or_create(user=user)

    submission = Submission.objects.create(
        learner=learner,
        course=question.course,
        score=question.marks if selected and selected.is_correct else 0,
        total_marks=question.marks,
    )
    return redirect("show_exam_result", submission_id=submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    passed = submission.score >= max(1, submission.total_marks * 0.5)
    return render(
        request,
        "exam_result.html",
        {"submission": submission, "passed": passed},
    )
