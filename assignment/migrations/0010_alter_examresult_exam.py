# Generated by Django 4.2.3 on 2023-08-15 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0009_alter_examresult_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresult',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_exam', to='assignment.exam'),
        ),
    ]
