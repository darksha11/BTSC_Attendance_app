# Generated by Django 2.2.5 on 2019-12-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('In_time', models.DateTimeField()),
                ('Out_time', models.DateTimeField()),
                ('currentdate', models.DateField()),
                ('locationn', models.CharField(max_length=150) ),
            ],
        ),
    ]
