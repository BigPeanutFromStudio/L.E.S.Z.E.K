# Generated by Django 5.1.6 on 2025-03-17 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leszek_app', '0002_alter_question_correct_answer_alter_question_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question',
        ),
    ]
