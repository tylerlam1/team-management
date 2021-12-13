from django.urls import path

from . import views

urlpatterns = [
    path("", views.TeammateListView.as_view(), name="get_users"),
    path("add", views.TeammateCreateView.as_view(), name="add_user"),
    path("edit/<int:pk>", views.TeammateUpdateView.as_view(), name="edit_user"),
    path("edit/<int:pk>/delete", views.TeammateDeleteView.as_view(), name="delete_user")
]