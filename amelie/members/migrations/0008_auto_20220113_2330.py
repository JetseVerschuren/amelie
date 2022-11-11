# Generated by Django 2.2.25 on 2022-01-13 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_person_nda'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='verified_on',
            field=models.DateField(blank=True, null=True, verbose_name='Verified on'),
        ),
        migrations.AddField(
            model_name='membershiptype',
            name='needs_verification',
            field=models.BooleanField(default=False, verbose_name='Needs verification'),
        ),
    ]
