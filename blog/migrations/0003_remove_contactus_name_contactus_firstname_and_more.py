# Generated by Django 4.2.3 on 2023-08-01 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='name',
        ),
        migrations.AddField(
            model_name='contactus',
            name='firstName',
            field=models.CharField(default='Fname', max_length=50),
        ),
        migrations.AddField(
            model_name='contactus',
            name='lastName',
            field=models.CharField(default='lName', max_length=50),
        ),
    ]
