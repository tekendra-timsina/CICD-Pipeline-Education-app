# Generated by Django 2.1.5 on 2019-04-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=100)),
                ('student_subject', models.CharField(max_length=100)),
                ('student_textfield', models.TextField(max_length=500)),
            ],
        ),
    ]
