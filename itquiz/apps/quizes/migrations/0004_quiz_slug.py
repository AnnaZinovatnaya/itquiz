# Generated by Django 2.2.2 on 2019-06-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_auto_20190623_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(default='python1'),
        ),
    ]
