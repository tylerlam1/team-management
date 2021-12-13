from django.urls import path

from . import views

urlpatterns = [
    path("", views.TeammateListView.as_view(), name="get_users"),
    path("add", views.TeammateCreateView.as_view(), name="add_user"),
    path("edit/<int:user_id>/", views.edit_user, name="edit_user")
]