from django.contrib import admin
from repository.models import Repository

class RepositoryAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'user', 'name', 'description', 'is_private', 'created', 'modified']

admin.site.register(Repository, RepositoryAdmin)
