from django.contrib import admin
from django.contrib.auth.hashers import identify_hasher
from .models import User

def is_password_hashed(password):
    try:
        identify_hasher(password)
        return True
    except ValueError:
        return False

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'role', 'is_staff')

    def save_model(self, request, obj, form, change):
        if not is_password_hashed(obj.password):
            obj.set_password(obj.password)
        obj.save()

admin.site.register(User, UserAdmin)