from django.contrib import admin
from user.models import Key

class KeyAdmin(admin.ModelAdmin):
    list_display = ['fingerprint', 'user', 'name', 'created', 'modified']

admin.site.register(Key, KeyAdmin)
