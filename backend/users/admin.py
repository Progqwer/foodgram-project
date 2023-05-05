from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser, Follow


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'first_name')


@admin.register(Follow)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
