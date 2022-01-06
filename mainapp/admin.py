from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from . import models

class Announcement_admin(SummernoteModelAdmin):
    summernote_fields = ('announcement_description', )

class Answers_admin(SummernoteModelAdmin):
    summernote_fields = ('answer', )

admin.site.register(models.VideoTeacher)
admin.site.register(models.VideoStudent)
admin.site.register(models.Question, Answers_admin)
admin.site.register(models.Announcement, Announcement_admin)