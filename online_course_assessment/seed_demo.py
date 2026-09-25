import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_course.settings")
import django
django.setup()

from django.contrib.auth.models import User
from courses.models import Instructor, Lesson, Course, Question, Choice, Learner

u, _ = User.objects.get_or_create(username="demo_learner", defaults={"first_name":"Demo","last_name":"Learner"})
i, _ = Instructor.objects.get_or_create(email="instructor@example.com", defaults={"name":"Demo Instructor"})
l1, _ = Lesson.objects.get_or_create(title="Introduction to Django", defaults={"content":"Django fundamentals and project structure.", "duration_minutes":30})
l2, _ = Lesson.objects.get_or_create(title="Django Models and ORM", defaults={"content":"Learn models, relationships and ORM queries.", "duration_minutes":45})
c, _ = Course.objects.get_or_create(name="Django Web Development", defaults={"description":"Build web applications with Django, templates, models and assessments.", "instructor":i})
c.instructor = i
c.lessons.set([l1,l2])
c.save()
q, _ = Question.objects.get_or_create(course=c, text="Which file defines Django URL patterns?", defaults={"marks":1})
Choice.objects.get_or_create(question=q, text="urls.py", defaults={"is_correct":True})
Choice.objects.get_or_create(question=q, text="models.py", defaults={"is_correct":False})
Choice.objects.get_or_create(question=q, text="admin.py", defaults={"is_correct":False})
Choice.objects.get_or_create(question=q, text="settings.py", defaults={"is_correct":False})
Learner.objects.get_or_create(user=u)
print("Demo data created. Course ID:", c.id, "Question ID:", q.id)
