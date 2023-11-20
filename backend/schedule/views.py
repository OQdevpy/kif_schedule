from django.shortcuts import render
from .serializers import *
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# Create your views here.


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DocumentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        qs = self.queryset
        if group := self.request.GET.get("gorup", None):
            qs = qs.filter(group=int(group))
        return qs


class BotUserListRetrieve(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
