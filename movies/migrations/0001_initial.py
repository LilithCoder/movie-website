# Generated by Django 3.0.6 on 2020-07-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=50)),
                ('screenwriter', models.CharField(max_length=50)),
                ('Starring', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('num_stars', models.DecimalField(decimal_places=2, max_digits=5)),
                ('length', models.IntegerField()),
            ],
            options={
                'ordering': ['num_stars'],
            },
        ),
    ]