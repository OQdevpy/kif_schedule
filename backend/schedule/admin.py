from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number','size','room_type']
    search_fields = ['number','size','room_type']
    list_filter = ['number','size','room_type']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['academic_code']
    search_fields = ['academic_code']
    list_filter = ['academic_code']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['group','subject','teacher','room','day','para']
    search_fields = ['group','subject','teacher','room','day','para']
    list_filter = ['group','subject','teacher','room','day','para']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title','file_url']
    search_fields = ['title','file_url']
    list_filter = ['title','file_url']

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['tg_id','username','full_name']
    search_fields = ['tg_id','username','full_name']
    list_filter = ['tg_id','username','full_name']