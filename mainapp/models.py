from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Announcement(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, null=True, unique_for_date='publish')
    announcement_description = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='all_projects')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('home:post_single', args=[self.slug])

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title

class VideoTeacher(models.Model):
    name = models.CharField(max_length=250)
    video = models.FileField(upload_to='video_lessons')

    def __str__(self):
        return self.name

class VideoStudent(models.Model):
    name = models.CharField(max_length=250)
    video = models.FileField(upload_to='video_lessons')

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=550)
    answer = models.TextField(null=True)
    answer_file = models.FileField(upload_to='video_lessons', default='settings.MEDIA_ROOT/media/anonymous.jpg')

    def __str__(self):
        return self.question
