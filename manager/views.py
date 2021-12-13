from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

from manager.forms import EditTeammateForm

from .models import Teammate

# Create your views here.
class TeammateListView(ListView):
    """
    Get all team members from the database.
    """
    template_name = "index.html"
    model = Teammate

class TeammateCreateView(CreateView):
    """
    Add a new team member to the database.
    """
    form_class = EditTeammateForm
    template_name = "add_user.html"
    success_url =  "/"

class TeammateUpdateView(UpdateView):
    """
    Edit a particular team member's database information.
    """
    form_class = EditTeammateForm
    model = Teammate
    template_name = "edit_user.html"
    success_url = "/"

class TeammateDeleteView(DeleteView):
    """
    Delete a particular team member's database record.
    """
    pass