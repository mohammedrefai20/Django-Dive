from django.shortcuts import render, get_object_or_404
from .models import instructor


def index(request):
    instructors = instructor.objects.prefetch_related('courses').all()
    return render(request, 'instructors/index.html', {'instructors': instructors})


def detail(request, pk):
    inst = get_object_or_404(instructor, pk=pk)
    courses = inst.courses.prefetch_related('students').all()
    return render(request, 'instructors/detail.html', {
        'instructor': inst,
        'courses': courses,
    })
