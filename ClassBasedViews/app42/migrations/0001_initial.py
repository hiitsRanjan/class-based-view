# Generated by Django 3.0.2 on 2020-10-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact_no', models.IntegerField(unique=True)),
                ('salary', models.FloatField()),
                ('photo', models.ImageField(upload_to='employee_image')),
                ('address', models.TextField()),
                ('email_id', models.CharField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]
