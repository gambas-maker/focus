from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth import get_user_model
=======

# Register your models here.
>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

<<<<<<< HEAD
=======

>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
<<<<<<< HEAD
    list_display = ['email', 'username',]
=======
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272

admin.site.register(CustomUser, CustomUserAdmin)