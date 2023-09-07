from rest_framework import serializers
from espacios.models import Espacio, Producto

class EspacioSerializer(serializers.ModelSerializer):
    nombre_spc = serializers.CharField(max_length=50,
    style={'placeholder': 'Nombre espacio', 'autofocus': True, 'hide_label': True})

    class Meta:
        model = Espacio
        fields = ['id', 'nombre_spc']

class ProductoSerializer(serializers.ModelSerializer):
    nombre_prod = serializers.CharField(max_length=50,
    style={'placeholder': 'Nombre producto', 'autofocus': True, 'hide_label': True})
    espacio_id = serializers.IntegerField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre_prod', 'espacio_id']


