# Generated by Django 3.0.3 on 2020-05-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Career', '0005_advance_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.IntegerField()),
                ('C_name', models.TextField()),
                ('nirf', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('fee', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('C_web', models.TextField()),
                ('C_details', models.TextField()),
            ],
        ),
    ]
