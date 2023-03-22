from django.contrib import admin
from .models import *


class CurseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'group', 'create_date', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description']
    list_filter = ['create_date']
    list_editable = ['is_published', ]


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file', 'author', 'create_date', 'curse']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'author']
    list_filter = ['create_date', 'title', 'author']


admin.site.register(Curse, CurseAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(GroupC)
