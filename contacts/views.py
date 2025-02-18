from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer


class ContactListView(ListView):
    model = Contact
    template_name = "contacts/contact_list.html"
    context_object_name = "contacts"
    paginate_by = 10


class ContactDetailView(DetailView):
    model = Contact
    template_name = "contacts/contact_detail.html"
    context_object_name = "contact"


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contacts/contact_form.html"
    fields = [
        "first_name",
        "last_name",
        "email",
        "mobile_phone",
        "website",
        "twitter_handle",
        "linkedin_profile",
        "birth_date",
        "address",
        "notes",
        "photo",
        "is_favourite",
    ]
    success_url = reverse_lazy("contacts:list")

    def form_valid(self, form):
        messages.success(self.request, "Contact created successfully!")
        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "contacts/contact_form.html"
    fields = [
        "first_name",
        "last_name",
        "email",
        "mobile_phone",
        "website",
        "twitter_handle",
        "linkedin_profile",
        "birth_date",
        "address",
        "notes",
        "photo",
        "is_favourite",
    ]
    success_url = reverse_lazy("contacts:list")

    def form_valid(self, form):
        messages.success(self.request, "Contact updated successfully!")
        return super().form_valid(form)


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "contacts/contact_confirm_delete.html"
    success_url = reverse_lazy("contacts:list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Contact deleted successfully!")
        return super().delete(request, *args, **kwargs)


@require_http_methods(["POST", "GET"])  # Allow both POST and GET for now
def toggle_favourite(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.is_favourite = not contact.is_favourite
    contact.save()

    # Check if request is from HTMX
    if request.htmx:
        return render(request, "contacts/_favourite_status.html", {"contact": contact})

    messages.success(
        request,
        f'Contact {"added to" if contact.is_favourite else "removed from"} favourites!',
    )
    return redirect("contacts:list")


class ContactListViewAPI(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def update(self, request, *args, **kwargs):
        contact = self.get_object()
        serializer = self.get_serializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
