from django.contrib import admin
from .models import *

# Register your models here.

class TrackBookAdmin(admin.ModelAdmin):
    """
        Admin config for Alert Mechanism in Recommendation Engines
    """
    model = TrackBook
    list_display = ('user_id', 'book_id', 'status', 'created')
    search_fields = ('user_id', 'book_id', 'created')
    list_filter = ('user_id', 'book_id', 'created')


admin.site.register(TrackBook, TrackBookAdmin)
