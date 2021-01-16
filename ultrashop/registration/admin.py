from registration.models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    class Meta:
        list_display = [field.name for field in User._meta.get_fields()]
