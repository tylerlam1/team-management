from django import forms
from django.views.generic import CreateView

from .models import Teammate

CREATE_FIELDS = [
    "first_name",
    "last_name",
    "phone_number",
    "email",
    "is_admin"
]

ADMIN_FIELDS = [
    (True, "Regular - Can't delete members"),
    (False, "Admin - Can delete members")
]

class EditTeammateForm(forms.ModelForm):
    """
    Add a new team member to the database.
    """
    class Meta:
        model = Teammate
        fields = CREATE_FIELDS
        widgets = {
            "is_admin": forms.RadioSelect(choices=ADMIN_FIELDS)
        }
    