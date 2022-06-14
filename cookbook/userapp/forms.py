from django.contrib.auth.forms import UserCreationForm
from .models import BookUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = BookUser
        fields = ('username', 'password1', 'password2', 'email')
