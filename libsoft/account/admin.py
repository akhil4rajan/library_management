from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .forms import libsoftCreationForm, libsoftChangeForm
from .models import User

admin.site.site_header = 'Lib Softnotions Administration'


class LibSoftAdmin(UserAdmin):
    """
    Admin config of User
    """
    add_form = libsoftCreationForm
    form = libsoftChangeForm
    model = User
    list_display = ['email', 'username', 'first_name', 'date_joined', 'is_active']


admin.site.register(User, LibSoftAdmin)
admin.site.register(Permission)
