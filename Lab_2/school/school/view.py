from django.shortcuts import render
from instructors.models import instructor
from students.models import Student
from courses.models import Course


def index(request):
    context = {
        'instructor_count': instructor.objects.count(),
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, 'home.html', context)
