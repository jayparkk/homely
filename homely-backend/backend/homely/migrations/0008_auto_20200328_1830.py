# Generated by Django 2.2.6 on 2020-03-29 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0007_auto_20200328_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(default='gallery/default.jpeg', upload_to='gallery'),
        ),
    ]