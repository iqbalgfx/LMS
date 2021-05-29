from django.shortcuts import render, get_object_or_404
from .models import Course
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

def course_list(request):
    object_list = Course.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        courses = paginator.page(paginator.num_pages)
    return render(request,
                    'courses/courses/list.html',
                    {'page': page,
                    'courses': courses})

def course_detail(request, year, month, day, course):
    course = get_object_or_404(Course, slug=course,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    course.visits = course.visits+1
    course.save()
    object_list = Course.published.all()
    return render(request,
                    'courses/courses/detail.html',
                    {'course': course})