from django.shortcuts import render
from .serializers import *
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        if kurs := self.request.GET.get("kurs", None):
            return self.queryset.filter(Q(kurs=int(kurs)), Q(is_active=True))
        return self.queryset.all()


class DocumentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Document.objects.filter(is_active=True)
    serializer_class = DocumentSerializer
    lookup_field = "title"


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "group"

    def get_queryset(self):
        qs = self.queryset
        if group := self.request.GET.get("gorup", None):
            qs = qs.filter(Q(group=int(group)) & Q(is_active=True))
        return qs
    @action(detail=True, methods=["GET"])
    def group(self, request, group=None):
        qs = self.queryset.filter(group=int(group)).order_by("day", "para")
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


class GetBotUserView(RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = "full_name"