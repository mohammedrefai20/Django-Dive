from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    courses = Course.objects.select_related('instructors').prefetch_related('students').all()
    return render(request, 'courses/index.html', {'courses': courses})


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = course.students.all()
    return render(request, 'courses/detail.html', {
        'course': course,
        'students': students,
    })
