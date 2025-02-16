from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Contact


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
        "is_favorite",
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
        "is_favorite",
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


def toggle_favorite(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.is_favorite = not contact.is_favorite
    contact.save()
    messages.success(
        request,
        f'Contact {"added to" if contact.is_favorite else "removed from"} favorites!',
    )
    return redirect("contacts:list")
