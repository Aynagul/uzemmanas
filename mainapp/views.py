from django.shortcuts import render, get_object_or_404
from .models import Announcement, VideoTeacher, VideoStudent, Question

def home(request):
    all_questions = Question.objects.all()

    return render(request, 'index.html', {'all_questions': all_questions})


def post_single(request, announcement):
    announcement = get_object_or_404(Announcement, slug=announcement, status='published')
    return render(request, 'announcementpage.html', {'announcement': announcement})


def eteacher(request):
    all_videoteacher = VideoTeacher.objects.all()
    return render(request, 'eteacher.html', {'all_videoteacher': all_videoteacher})


def estudent(request):
    all_videostudent = VideoStudent.objects.all()
    return render(request, 'estudent.html', {'all_videostudent': all_videostudent})

def announcementslist(request):
    all_announcements = Announcement.newmanager.all()
    return render(request, 'announcementslist.html', {'all_announcements': all_announcements})