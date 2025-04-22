from django.contrib import admin
from .models import Poll, PollOption, Vote

class PollOptionInline(admin.TabularInline):
    model = PollOption
    extra = 0
    readonly_fields = ('votes',)
    show_change_link = True

class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'uuid', 'created_at')
    inlines = [PollOptionInline]
    search_fields = ('title', 'id')
    readonly_fields = ('id', 'created_at')

    def uuid(self, obj):
        return obj.id
    uuid.short_description = 'UUID'

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll', 'option')
    list_filter = ('poll', 'option', 'user')
    search_fields = ('user__username', 'poll__title', 'option__option_text')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)

