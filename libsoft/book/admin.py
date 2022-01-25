from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    """
        Admin config for Alert Mechanism in Recommendation Engines
    """
    model = Book
    list_display = ('name', 'author', 'year_of_publication', 'availability', 'status', 'created')
    search_fields = ('name', 'author', 'year_of_publication', 'created')
    list_filter = ('author', 'year_of_publication', 'availability', 'created')


admin.site.register(Book, BookAdmin)
