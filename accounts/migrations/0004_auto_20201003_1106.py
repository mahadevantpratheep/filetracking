# Generated by Django 3.1.2 on 2020-10-03 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201002_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permission',
            name='myfile',
            field=models.FileField(default='documents/defimage.jpg', upload_to='documents/%Y/%m/%d'),
        ),
    ]
