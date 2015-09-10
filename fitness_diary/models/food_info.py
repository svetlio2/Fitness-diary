from django.db import models


# every field in FoodInfo is for 100g
class FoodInfo(models.Model):
    proteins = models.FloatField()
    carbs    = models.FloatField()
    fats     = models.FloatField()
    calories = models.FloatField()

    class Meta:
        app_label = 'fitness_diary'
