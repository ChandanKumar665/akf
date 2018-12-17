# Generated by Django 2.1.2 on 2018-12-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geo_Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('district', models.CharField(default=None, max_length=255)),
                ('block', models.CharField(default=None, max_length=255)),
                ('cluster', models.CharField(default=None, max_length=255)),
                ('gram_panchayat', models.CharField(default=None, max_length=255)),
            ],
            options={
                'db_table': 'geo_information',
            },
        ),
        migrations.CreateModel(
            name='Student_Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(default=None, max_length=255)),
                ('addition', models.IntegerField(default=0)),
                ('subtraction', models.IntegerField(default=0)),
                ('product', models.IntegerField(default=0)),
                ('division', models.IntegerField(default=0)),
                ('district_id', models.ForeignKey(on_delete=True, to='akf_app.Geo_Information')),
            ],
            options={
                'db_table': 'student_report',
            },
        ),
    ]
