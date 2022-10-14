from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import  User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username",
        "email",
        "address",
        "phone_number",
        "is_staff",
        "is_superuser",]
        
    readonly_fields = ["is_superuser",
        "user_permissions",
        "groups",
        "date_joined",
        "is_active",
        "last_login",]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields

admin.site.register(User,UserAdmin)
