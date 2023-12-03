from django.contrib.auth import authenticate
from rest_framework import serializers
from espacios.models import Espacio, Producto, Orden, OrdenProducto

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Usuario",write_only=True)
    password = serializers.CharField(label="Contraseña",style={'input_type': 'password'},trim_whitespace=False,write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Acceso denegado, usuario o contraseña incorrecta.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Usuario y contraseña requeridos.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

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
    precio = serializers.IntegerField(style={'placeholder': 'Precio', 'autofocus': True, 'hide_label': True})
    espacio_id = serializers.IntegerField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre_prod', 'espacio_id', 'precio']

    def validate_nombre_prod(self, value):
        nombre_ingresado = value
        instance = self.instance
        queryset = Producto.objects.exclude(pk=instance.pk) if instance else Producto.objects.all()

        if nombre_ingresado and queryset.filter(nombre_prod__exact=nombre_ingresado).exists():
            raise serializers.ValidationError("Nombre de producto ya ingresado!")

        return value

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
    
    