from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from reservas import views
from django.contrib import admin

urlpatterns = [
    path('reservas/', views.ReservasIndex.as_view(), name='reservas'),

    path('reservas/crearReserva/', views.ReservaCreate.as_view(), name='crear_reserva'),
    #path('reservas/verReserva/<int:id>', views.ReservaView.as_view(), name='ver_reserva'),
]

urlpatterns = format_suffix_patterns(urlpatterns)