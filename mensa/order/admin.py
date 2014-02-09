from django.contrib import admin
from order.models import Meal, Day

class MealInline(admin.TabularInline):
    model = Meal
    extra = 3

class DayAdmin(admin.ModelAdmin):
    inlines = [MealInline]
    list_display = ('date', 'is_from_this_week')
    list_filter = ['date']

admin.site.register(Day,DayAdmin)
