# Generated by Django 5.1.1 on 2024-10-30 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0003_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='marks',
            new_name='Marks',
        ),
    ]
