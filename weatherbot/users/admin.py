from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "tg_id", "status", )
    search_fields = ("status", "id", )
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
