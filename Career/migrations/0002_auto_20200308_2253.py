# Generated by Django 3.0.3 on 2020-03-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='Question',
            field=models.TextField(),
        ),
    ]
