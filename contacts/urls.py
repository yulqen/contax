# crud urls for the contacts app

from django.urls import path

from . import views
from .views import ContactDetailViewAPI, ContactListViewAPI

app_name = "contacts"

urlpatterns = [
    path("", views.ContactListView.as_view(), name="list"),
    path("<int:pk>/", views.ContactDetailView.as_view(), name="detail"),
    path("create/", views.ContactCreateView.as_view(), name="create"),
    path(
        "<int:pk>/update/",
        views.ContactUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        views.ContactDeleteView.as_view(),
        name="delete",
    ),
    path("toggle_favourite/<int:pk>/", views.toggle_favourite, name="toggle-favourite"),
    path("api/contacts/", ContactListViewAPI.as_view(), name="contact-list"),
    path(
        "api/contacts/<int:pk>/", ContactDetailViewAPI.as_view(), name="contact-detail"
    ),
]
