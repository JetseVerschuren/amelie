# Generated by Django 3.2.16 on 2022-10-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_alter_study_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(editable=False, max_length=150),
        ),
    ]
