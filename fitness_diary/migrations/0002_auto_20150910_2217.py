# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_diary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('foods', models.ManyToManyField(to='fitness_diary.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='foodprogram',
            name='nutritions',
            field=models.ManyToManyField(to='fitness_diary.Nutrition'),
            preserve_default=True,
        ),
    ]
