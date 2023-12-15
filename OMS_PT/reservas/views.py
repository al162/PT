from collections import Counter

from reservas.models import Reserva, Mesa
from reservas.serializers import MesaSerializer,ReservaSerializer 
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import permissions
from . import serializers
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout

class ReservasIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index_reservas.html'

    def get(self, request):
        queryset = Reserva.objects.all()
        return Response({'reserva': queryset})

class ReservaCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "crear_reserva.html"
    style = {'template_pack': 'rest_framework/horizontal/'}

    def get(self, request):
        serializer = ReservaSerializer()
        return Response({'serializer': serializer, 'style': self.style})


