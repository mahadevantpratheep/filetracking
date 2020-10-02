# Generated by Django 3.1.2 on 2020-10-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='venue',
        ),
        migrations.AddField(
            model_name='permission',
            name='myfile',
            field=models.FileField(default=13, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
