from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


school_courses = [
    {"name": "Python", "duration": "2 months", "cost": "25k"},
    {"name": "Android", "duration": "3 months", "cost": "35k"},
    {"name": "Data Science", "duration": "4 months", "cost": "60k"},
]


def courses(request):
    context = {"school_courses": school_courses}
    return render(request, 'courses.html', context)