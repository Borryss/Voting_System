from django.contrib import admin

from .models import Poll


# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')


admin.site.register(Poll, PollAdmin)