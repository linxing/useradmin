from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('username', 'server', 'due_date')
    list_per_page = 50
    actions_on_bottom = True
    actions_on_top = True

    actions_selection_counter = True
    list_filter = ('username', 'server')

    search_fields = ('username', 'server')

    admin.site.index_title = 'UserAdmin'
    admin.site.site_title = 'UserAdminTitle'


# admin.site.register(User)