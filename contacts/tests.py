import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Contact


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def contact(db):
    return Contact.objects.create(
        first_name="Mark",
        last_name="Chippendale",
        email="mark@gmail.com",
        mobile_phone="+1234567890",
        website="https://example.com",
        is_favourite=False,
    )


@pytest.mark.filterwarnings("ignore::django.utils.deprecation.RemovedInDjango60Warning")
@pytest.mark.django_db
class TestContactsAPI:
    def test_create_contact(self, api_client):
        response = api_client.post(
            "/api/contacts/",
            data={
                "first_name": "Mark",
                "last_name": "Chippendale",
                "email": "mark@gmail.com",
                "mobile_phone": "+1234567892",
                "website": "https://example.com",
                "is_favourite": False,
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert "id" in response.data

    def test_list_contacts(self, api_client, contact):
        response = api_client.get("/api/contacts/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1

    def test_retrieve_contact(self, api_client, contact):
        response = api_client.get(f"/api/contacts/{contact.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == contact.id

    def test_update_contact(self, api_client, contact):
        response = api_client.put(
            f"/api/contacts/{contact.id}/",
            data={"first_name": "Robert", "last_name": "Doe"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["first_name"] == "Robert"

    def test_delete_contact(self, api_client, contact):
        response = api_client.delete(f"/api/contacts/{contact.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert (
            api_client.get(f"/api/contacts/{contact.id}/").status_code
            == status.HTTP_404_NOT_FOUND
        )


@pytest.mark.filterwarnings("ignore::django.utils.deprecation.RemovedInDjango60Warning")
@pytest.mark.django_db
class TestContactsViews:
    def test_contact_create_view(self, api_client):
        response = api_client.post(
            reverse("contacts:create"),
            data={
                "first_name": "Mark",
                "last_name": "Chippendale",
                "email": "mark@gmail.com",
                "mobile_phone": "+1234567890",
                "website": "https://example.com",
                "is_favourite": False,
            },
        )
        assert response.status_code == status.HTTP_302_FOUND
        assert Contact.objects.filter(first_name="Mark").exists()

    def test_contact_list_view(self, api_client, contact):
        response = api_client.get(reverse("contacts:list"))
        assert response.status_code == status.HTTP_200_OK
        assert contact.first_name in str(response.content)

    def test_contact_detail_view(self, api_client, contact):
        response = api_client.get(reverse("contacts:detail", kwargs={"pk": contact.id}))
        assert response.status_code == status.HTTP_200_OK
        assert contact.first_name in str(response.content)

    def test_contact_update_view(self, api_client, contact):
        response = api_client.post(
            reverse("contacts:update", kwargs={"pk": contact.id}),
            data={
                "first_name": "Robert",
                "last_name": "Doe",
                "email": "robert.doe@example.com",
                "mobile_phone": "+1234567890",
                "website": "https://example.com",
                "is_favourite": False,
            },
        )
        assert response.status_code == status.HTTP_302_FOUND
        contact.refresh_from_db()
        assert contact.first_name == "Robert"

    def test_contact_delete_view(self, api_client, contact):
        response = api_client.post(
            reverse("contacts:delete", kwargs={"pk": contact.id})
        )
        assert response.status_code == status.HTTP_302_FOUND
        assert not Contact.objects.filter(id=contact.id).exists()
