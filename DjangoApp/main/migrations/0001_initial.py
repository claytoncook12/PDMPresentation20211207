# Generated by Django 3.2.9 on 2021-12-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MP3Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=300, verbose_name='File Name')),
                ('mp3_audio_file', models.FileField(upload_to='')),
            ],
        ),
    ]
