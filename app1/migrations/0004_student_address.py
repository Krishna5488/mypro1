# Generated by Django 5.1.4 on 2024-12-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
