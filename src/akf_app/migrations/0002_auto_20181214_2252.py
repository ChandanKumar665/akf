# Generated by Django 2.1.2 on 2018-12-14 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akf_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geo_information',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='geo_information',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student_report',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student_report',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student_report',
            name='district_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_id', to='akf_app.Geo_Information'),
        ),
    ]
