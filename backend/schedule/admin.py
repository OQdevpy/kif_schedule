from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'size', 'room_type', 'id']
    search_fields = ['number', 'size', 'room_type']
    list_filter = ['number', 'size', 'room_type']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['academic_code', 'id']
    search_fields = ['academic_code']
    list_filter = ['academic_code']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['group', 'subject', 'teacher', 'room', 'day', 'para', 'id']
    search_fields = ['group', 'subject', 'teacher', 'room', 'day', 'para']
    list_filter = ['group', 'subject', 'teacher', 'room', 'day', 'para']


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
