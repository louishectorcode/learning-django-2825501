from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	# Use to provide a more adapted view of the rows and colums
    list_display = ['name', 'species', 'breed', 'age', 'sex']
