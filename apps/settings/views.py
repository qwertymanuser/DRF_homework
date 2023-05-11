from django.shortcuts import render
from .models import Setting,About,Slide,Course
# Create your views here.
def index(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    slide = Slide.objects.latest("id")
    course = Course.objects.all()
    context = {
        'setting': setting,
        'about':about,
        'slide':slide,
        'course':course,
    }
    return render(request, "index.html", context)

def contact(request):
    setting = Setting.objects.latest("id")
    context = {
        'setting': setting
    }
    return render(request, "contact.html", context)