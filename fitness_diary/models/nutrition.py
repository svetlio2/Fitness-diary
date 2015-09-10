from django.db import models
from fitness_diary.models.food import Food


class Nutrition(models.Model):
    time  = models.TimeField()
    foods = models.ManyToManyField(Food)

    class Meta:
        app_label = 'fitness_diary'
