from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_users, name="get_users"),
    path("add", views.add_user, name="add_user"),
    path("edit", views.edit_user, name="edit_user")
]