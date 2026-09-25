from django.contrib import admin
from .models import (
    Instructor,
    Learner,
    Course,
    Lesson,
    Question,
    Choice,
    Submission,
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "course", "marks")
    list_filter = ("course",)
    inlines = [ChoiceInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "instructor")
    search_fields = ("name", "description")
    inlines = [QuestionInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_minutes")
    search_fields = ("title", "content")


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "text", "is_correct")
    list_filter = ("is_correct",)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("learner", "course", "score", "total_marks", "submitted_at")
    list_filter = ("course",)
