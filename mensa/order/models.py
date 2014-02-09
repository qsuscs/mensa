from django.db import models
from django.utils import timezone

class Day(models.Model):
    date = models.DateTimeField('date')

    def __unicode__(self):
        return self.date.strftime('%Y-%m-%d')

    def is_from_this_week(self):
        return self.date.strftime('%W') == timezone.now().strftime('%W') # TODO: Can be done better.
    is_from_this_week.admin_order_field = 'date'
    is_from_this_week.boolean = True
    is_from_this_week.short_description = 'Is from this week?'

class Meal(models.Model):
    day = models.ForeignKey(Day)
    meal_text = models.CharField(max_length=200)
    orders = models.IntegerField(default=0)

    def __unicode__(self):
        return self.meal_text
