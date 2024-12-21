from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import RatingForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'examapp/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            new_rating = form.cleaned_data['rating']
            course.update_rating(new_rating)
            return redirect('course_detail', pk=course.id)
    else:
        form = RatingForm()
    
    return render(request, 'course_detail.html', {'course': course, 'form': form})

def home(request):
    courses = Course.objects.all() 
    return render(request, 'examapp/home.html', {'courses': courses})