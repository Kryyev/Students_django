from django.urls import path

from .views import create_student
from .views import delete_student
from .views import detail_student
from .views import get_students
from .views import update_student


app_name = 'student'

urlpatterns = [
    path('create/', create_student, name='create'),
    path('', get_students, name='list'),
    path('detail/<int:student_id>/', detail_student, name='detail'),
    path('update/<int:student_id>/', update_student, name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
