from django_registration.forms import RegistrationForm
from .models import User


class UserForm(RegistrationForm):
    """
    User registration form
    """
    class Meta(RegistrationForm.Meta):
        model = User
