from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class libsoftCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class libsoftChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
