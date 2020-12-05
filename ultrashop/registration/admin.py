from registration.models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ['id', 'username', 'first_name', 'last_name', 'email',
                        'last_login', 'is_active', 'birth_date', 'is_staff',
                        'bio', 'birth_date', 'date_joined', 'is_superuser',
                        'is_active', 'date_joined', 'location', ]