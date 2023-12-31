# Generated by Django 4.2.3 on 2023-07-27 08:12

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='courses/')),
                ('field', models.CharField(choices=[('FRONT-END', 'Front End'), ('BACK-END', 'Back End'), ('FULLSTACK', 'Full stack'), ('MOBILE-DEVELOPMENT', 'Mobile Development'), ('GRAPHIC-DESIGN', 'Graphic Design'), ('MOTION-GRAPHICS', 'Motion Graphics'), ('MARKETING', 'Marketing'), ('PHOTOGRAPHY', 'Photography'), ('OTHER', 'Other')], max_length=30)),
                ('question_number', models.PositiveIntegerField()),
                ('total_marks', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('video', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
