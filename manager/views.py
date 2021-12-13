from django.http import HttpResponse
from django.views.generic import ListView, CreateView

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
    template_name = "add_user.html"
    model = Teammate
    fields = ["first_name", "last_name", "phone_number", "email"]
    success_url =  "/"

def edit_user(request, user_id):
    """
    Edit a particular team member's database information.
    """
    return HttpResponse("Edit a team member here.")