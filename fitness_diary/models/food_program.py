from django.db import models

from fitness_diary.models.nutrition import Nutrition


class FoodProgram(models.Model):
    nutritions = models.ManyToManyField(Nutrition)

    class Meta:
        app_label = 'fitness_diary'
