from rest_framework import serializers
from reservas.models import Mesa, Reserva

class MesaSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField()
    size = serializers.CharField()
    min_sillas = serializers.IntegerField()
    max_sillas = serializers.IntegerField()

    class Meta:
        model = Mesa
        fields = "__all__"

class ReservaSerializer(serializers.ModelSerializer):
    mesa_id = serializers.IntegerField()
    user_id = serializers.IntegerField(style={'placeholder': 'Rut', 'autofocus': True, 'hide_label': True})
    fecha = serializers.DateTimeField()
    sillas = serializers.IntegerField()

    class Meta:
        model = Reserva
        fields = "__all__"