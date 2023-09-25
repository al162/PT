from rest_framework import serializers
from espacios.models import Espacio, Producto, Orden, OrdenProducto

class EspacioSerializer(serializers.ModelSerializer):
    nombre_spc = serializers.CharField(max_length=50,
    style={'placeholder': 'Nombre espacio', 'autofocus': True, 'hide_label': True})

    class Meta:
        model = Espacio
        fields = ['id', 'nombre_spc']

class ProductoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    nombre_prod = serializers.CharField(max_length=50,
    style={'placeholder': 'Nombre producto', 'autofocus': True, 'hide_label': True})
    espacio_id = serializers.IntegerField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre_prod', 'espacio_id']

class OrdenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProducto
        fields = ['orden','producto', 'cantidad']
    
class OrdenSerializer(serializers.ModelSerializer):
    productos = OrdenProductoSerializer(many=True)
    
    class Meta:
        model = Orden
        fields = '__all__'
    
    def create(self, validated_data):
        productos_data = validated_data.pop('productos')

        for producto_data in productos_data:
            cantidad = producto_data.pop('cantidad')
            producto = producto_data.pop('producto')
            orden = producto_data.pop('orden')
            OrdenProducto.objects.create(orden= orden, producto=producto, cantidad=cantidad)

        return orden
    
    