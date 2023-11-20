from django.shortcuts import render
from .serializers import *
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
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
    lookup_field = "group"

    def get_queryset(self):
        qs = self.queryset
        if group := self.request.GET.get("gorup", None):
            qs = qs.filter(group=int(group))
        return qs
    @action(detail=True, methods=["GET"])
    def group(self, request, group=None):
        qs = self.queryset.filter(group=int(group))
        days = ("Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba")
        data = {
            day: self.get_serializer(qs.filter(day=day), many=True).data
            for day in days
        }
        return Response(data)


class BotUserListRetrieve(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = "tg_id"
