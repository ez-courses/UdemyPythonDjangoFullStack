from django.contrib import admin

# Register your models here.
from .models import Movie, Customer


class MovieAdmin(admin.ModelAdmin):
    # Control the order of fields displayed in admin site
    fields = ['release_year', 'title', 'length']

    search_fields = ['release_year', 'title']

    list_filter = ['release_year', 'title', 'length']

    list_display = ['title', 'release_year', 'length']

    list_editable = ['release_year']


admin.site.register(Customer)
admin.site.register(Movie, MovieAdmin)
