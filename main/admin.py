from django.contrib import admin

from .models import Project, ContactMessage



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "technologies",
        "created_at",
    )

    search_fields = (
        "title",
        "technologies",
    )

    list_filter = (
        "created_at",
    )





@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "message",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "message",
    )

    list_filter = (
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )