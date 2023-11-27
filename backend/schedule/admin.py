from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "KIF BOT Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "KIF BOT"


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'room', 'size', 'room_type',]
    search_fields = ['room', 'size', 'room_type']
    list_filter = ['room', 'size', 'room_type']
    list_display_links = ['id', 'room', ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'academic_code', 'kurs']
    search_fields = ['academic_code', 'kurs']
    list_filter = ['academic_code', 'kurs']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'subject', 'lesson_type', 'teacher', 'room', 'day', 'para', 'week']
    search_fields = ['group', 'subject', 'lesson_type', 'teacher', 'room', 'day', 'para', 'week']
    list_filter = ['group', 'subject', 'lesson_type', 'teacher', 'room', 'day', 'para', 'week']
    list_display_links = ['id', 'group', ]
    list_editable = ['day', 'para']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file_url_tag',]
    search_fields = ['title', 'file_url']
    list_filter = ['title', 'file_url']
    list_display_links = ['id', 'title', ]


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'username', 'full_name', 'phone_number', 'id']
    search_fields = ['tg_id', 'username', 'full_name', 'phone_number']
    list_filter = ['tg_id', 'username', 'full_name', 'phone_number']
