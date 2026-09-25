from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    lessons = models.ManyToManyField("Lesson", blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    duration_minutes = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.title


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.text[:80]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Submission(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    total_marks = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.learner} - {self.score}/{self.total_marks}"
