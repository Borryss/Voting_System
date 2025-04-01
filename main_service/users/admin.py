from django.contrib import admin

from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'created_at', 'is_verified')
    search_fields = ('email', 'username')
    list_filter = ('is_verified',)

admin.site.register(User, UserAdmin)