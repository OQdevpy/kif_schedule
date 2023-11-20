from .models import *
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Group
        fields = "__all__"

class ScheduleSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source = "group.academic_code")
    room = serializers.CharField(source = "room.number")
    room_type = serializers.CharField(source = "room.room_type")
    subject = serializers.CharField(source = "subject.name")
    teacher = serializers.CharField(source = "teacher.name")
    
    class Meta:
        model = Schedule
        fields = "__all__"
    
# write sz for Document and BotUser
class DocumentSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Document
        fields = "__all__"

class BotUserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = BotUser
        fields = "__all__"