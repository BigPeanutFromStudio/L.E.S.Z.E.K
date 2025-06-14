# Generated by Django 5.1.6 on 2025-03-03 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10000)),
                ('answer_a', models.CharField(max_length=5000)),
                ('asnwer_b', models.CharField(max_length=5000)),
                ('answer_c', models.CharField(max_length=5000)),
                ('answer_d', models.CharField(max_length=5000)),
                ('correct_answer', models.CharField(max_length=5000, null=True)),
                ('media', models.CharField(max_length=5000, null=True)),
                ('code_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='leszek_app.code')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.CharField(max_length=5000)),
                ('sent_at', models.DateTimeField()),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='leszek_app.question')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='leszek_app.user')),
            ],
        ),
    ]
