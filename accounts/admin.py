from django.contrib import admin
from django.contrib.admin import ModelAdmin
from accounts.models import UserProfile


class UserProfileAdmin(ModelAdmin):

    list_display = ['id', 'user', 'address', 'phone', 'gender']
    list_display_links = ['id']
    ordering = ['id']
    list_filter = ['accepted_terms']
    search_fields = ['username']
    fieldsets = (('Important information',
                  {'fields': ['user'], 'description': 'This is yhe important part'}),
                 (None, {'fields': ['phone', 'gender', 'accepted_terms']}))


admin.site.register(UserProfile, UserProfileAdmin)
