from django.db import models

class Day(models.Model):
    date = models.DateTimeField('date')

    def __unicode__(self):
        return self.date.strftime('%Y-%m-%d')

class Meal(models.Model):
    day = models.ForeignKey(Day)
    meal_text = models.CharField(max_length=200)
    orders = models.IntegerField(default=0)

    def __unicode__(self):
        return self.meal_text
