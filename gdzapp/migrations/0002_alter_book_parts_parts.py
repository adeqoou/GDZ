# Generated by Django 5.0.3 on 2024-03-11 17:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdzapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='parts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.PositiveIntegerField(default=1)),
                ('tasks', models.ManyToManyField(to='gdzapp.task')),
            ],
        ),
    ]
