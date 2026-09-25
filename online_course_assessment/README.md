# Online Course App — Assessment Feature

This project implements the Final Project requirements:
- Question, Choice and Submission models
- Django admin inlines/admin classes
- Bootstrap course-details template
- Exam submission and result views
- URL routes for submit/show_exam_result
- Mock exam result page with Congratulations message

## Run locally

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Course page: http://127.0.0.1:8000/course/1/
- Admin: http://127.0.0.1:8000/admin/
- Mock exam result: http://127.0.0.1:8000/exam/result/1/

The database is SQLite and can be populated from the admin site.
