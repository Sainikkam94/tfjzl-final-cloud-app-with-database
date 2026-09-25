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


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "course", "marks")
    list_filter = ("course",)
    inlines = [ChoiceInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "instructor")
    search_fields = ("name", "description")
    inlines = [QuestionInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_minutes")
    search_fields = ("title", "content")


class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


class LearnerAdmin(admin.ModelAdmin):
    list_display = ("user",)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "text", "is_correct")
    list_filter = ("is_correct",)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("learner", "course", "score", "total_marks", "submitted_at")
    list_filter = ("course",)


admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)