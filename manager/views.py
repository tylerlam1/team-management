from django.http import HttpResponse

# Create your views here.
def get_users(request):
    """
    Get all team members from the database.
    """
    return HttpResponse("test response here.")

def add_user(request):
    """
    Add a new team member to the database.
    """
    return HttpResponse("Add a new team member here.")

def edit_user(request):
    """
    Edit a particular team member's database information.
    """
    return HttpResponse("Edit a team member here.")