# Generated by Django 2.2.17 on 2020-11-03 21:20
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0001_initial'),
        ('activities', '0003_auto_20190613_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='oauth_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oauth2_provider.Application'),
        ),
        migrations.AlterField(
            model_name='enrollmentoption',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity'),
        ),
        migrations.AlterField(
            model_name='enrollmentoption',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='enrollmentoptionanswer',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='enrollmentoptionanswer',
            name='enrollment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar.Participation'),
        ),
        migrations.AlterField(
            model_name='enrollmentoptionanswer',
            name='enrollmentoption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Enrollmentoption'),
        ),
        migrations.AlterField(
            model_name='enrollmentoptionfoodanswer',
            name='dishprice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='activities.DishPrice', verbose_name='Dish cost'),
        ),
        migrations.AlterField(
            model_name='enrollmentoptionselectboxanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.SelectboxOption', verbose_name='Respons'),
        ),
        migrations.AlterField(
            model_name='eventdeskregistrationmessage',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.Activity'),
        ),
        migrations.AlterField(
            model_name='selectboxoption',
            name='selection_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.EnrollmentoptionSelectbox'),
        ),
    ]
