from django.contrib import admin

from .models import Contact

site = admin.site

site.site_header = "Contax Admin"
site.site_title = "Contax Admin"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "mobile_phone", "is_favourite")
    list_filter = ("is_favourite", "created_at")
    search_fields = ("first_name", "last_name", "email", "notes")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Personal Information",
            {"fields": ("first_name", "last_name", "birth_date", "photo")},
        ),
        ("Contact Details", {"fields": ("email", "mobile_phone", "address")}),
        (
            "Online Presence",
            {"fields": ("website", "twitter_handle", "linkedin_profile")},
        ),
        ("Additional Information", {"fields": ("notes", "is_favourite")}),
        (
            "System Fields",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    ordering = ("last_name", "first_name")
    list_per_page = 20
