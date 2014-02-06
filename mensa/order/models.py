from django.db import models

class Day(models.Model):
    date = models.DateTimeField('date')

class Meal(models.Model):
    day = models.ForeignKey(Day)
    meal_text = models.CharField(max_length=200)
    orders = models.IntegerField(default=0)
