# Generated by Django 3.0.5 on 2020-07-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gfname', models.CharField(max_length=50)),
                ('coname1', models.CharField(max_length=100)),
                ('subname', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=10)),
                ('s_time', models.TimeField()),
                ('e_time', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
                ('topic1', models.CharField(max_length=50)),
                ('topic2', models.CharField(max_length=50)),
                ('topic3', models.CharField(max_length=50)),
                ('topic4', models.CharField(max_length=50)),
                ('tf', models.CharField(max_length=150)),
                ('c_agree', models.PositiveIntegerField()),
                ('agree', models.PositiveIntegerField()),
                ('disagree', models.PositiveIntegerField()),
                ('c_disagree', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
            ],
        ),
    ]