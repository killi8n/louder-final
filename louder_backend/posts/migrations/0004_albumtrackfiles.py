# Generated by Django 2.0.5 on 2018-05-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_album_track_file_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumTrackFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_file', models.FileField(upload_to='')),
            ],
        ),
    ]
