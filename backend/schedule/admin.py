from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "KIF BOT Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "KIF BOT"

@admin.register(Para)
class ParaAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'para', 'time_start', 'time_end', 'is_active']
    search_fields = ['para']
    list_filter = ['para']
    list_display_links = ['id', 'para', ]
    
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'room', 'size', 'room_type', 'is_active']
    search_fields = ['room', 'size', 'room_type']
    list_filter = ['room', 'size', 'room_type']
    list_display_links = ['id', 'room', ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'is_active']
    search_fields = ['name']
    list_filter = ['name']
    list_editable = ['is_active']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'academic_code', 'kurs', 'is_active']
    search_fields = ['academic_code', 'kurs']
    list_filter = ['academic_code', 'kurs']
    list_editable = ['is_active']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    search_fields = ['name']
    list_editable = ['is_active']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'subject', 'lesson_type', 'teacher', 'room', 'day', 'para', 'week', 'semester','is_active']
    search_fields = ['group', 'subject', 'lesson_type', 'teacher', 'room', 'day', 'para', 'week']
    list_filter = ['group', 'subject', 'lesson_type', 'teacher', 'room', 'day', 'para', 'week', 'is_active', 'semester']
    list_display_links = ['id', 'group', ]
    list_editable = ['lesson_type', 'day', 'para', 'week', 'is_active', 'semester']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'file_url_tag',  'is_active']
    search_fields = ['title', 'file_url']
    list_filter = ['title', 'file_url']
    list_display_links = ['id', 'title', ]
    list_editable = ['is_active']


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'username', 'full_name', 'phone_number', 'id']
    search_fields = ['tg_id', 'username', 'full_name', 'phone_number']
    list_filter = ['tg_id', 'username', 'full_name', 'phone_number']
