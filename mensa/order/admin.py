from django.contrib import admin
from order.models import Meal, Day

class MealInline(admin.TabularInline):
    model = Meal
    extra = 3

class DayAdmin(admin.ModelAdmin):
    inlines = [MealInline]

admin.site.register(Day,DayAdmin)
