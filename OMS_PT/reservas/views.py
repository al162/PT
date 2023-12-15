from collections import Counter

from reservas.models import Reserva, Mesa
from espacios.serializers import EspacioSerializer, ProductoSerializer, OrdenSerializer, LoginSerializer
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
    template_name = 'index_reserva.html'

    def get(self, request):
        queryset = Reserva.objects.all()
        return Response({'reserva': queryset})
    