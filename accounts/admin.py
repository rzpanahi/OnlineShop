from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]
    list_filter = ["is_active", "is_superuser", "is_staff",]
    search_fields = ["username", "first_name", "last_name", "email"]

    def delete_queryset(self, request, queryset):
        for user in queryset:
            user.delete()


admin.site.register(User, UserAdmin)