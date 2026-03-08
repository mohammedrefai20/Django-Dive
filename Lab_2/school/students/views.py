from django.shortcuts import render, get_object_or_404
from .models import Student


def index(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'students/index.html', {'students': students})


def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    courses = student.courses.select_related('instructors').prefetch_related('students').all()
    return render(request, 'students/detail.html', {
        'student': student,
        'courses': courses,
    })
