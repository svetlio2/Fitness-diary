from django.db import models
from fitness_diary.models.food_info import FoodInfo


class Food(models.Model):
    food_info = models.ForeignKey(FoodInfo)
    quantity  = models.IntegerField()

    class Meta:
        app_label = 'fitness_diary'
