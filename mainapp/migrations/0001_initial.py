# Generated by Django 3.2.1 on 2022-01-06 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=550)),
                ('answer', models.TextField(null=True)),
                ('answer_file', models.FileField(default='settings.MEDIA_ROOT/media/anonymous.jpg', upload_to='video_lessons')),
            ],
        ),
        migrations.CreateModel(
            name='VideoStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='video_lessons')),
            ],
        ),
        migrations.CreateModel(
            name='VideoTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='video_lessons')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=250, null=True, unique_for_date='publish')),
                ('announcement_description', models.TextField(null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
    ]