from collections import Counter

from espacios.models import Espacio, Producto, Orden, OrdenProducto
from reservas.models import Reserva, Mesa
from espacios.serializers import EspacioSerializer, ProductoSerializer, OrdenSerializer, LoginSerializer
from reservas.serializers import ReservaSerializer, MesaSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib import messages
from rest_framework import permissions
from . import serializers
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return redirect('espacios')
        else:
            return redirect('login')
        
class LogoutView(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return redirect('login')
    
#Vista para el indice de espacios
class EspacioIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index_espacio.html'

    def get(self, request):
        queryset = Espacio.objects.all()
        return Response({'espacios': queryset})
    
    def delete(request, pk):
        espacio = Espacio.objects.get(pk = pk)
        productos = Producto.objects.filter(espacio_id = pk)
        for producto in productos:
            producto.delete()
        espacio.delete()
        return redirect('espacios')
    
#Vista para crear un nuevo espacio    
class EspacioCreate(APIView):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'crear_espacio.html'

    def get(self, request):
        serializer = EspacioSerializer()
        return Response({'serializer': serializer})
    
    def post(self, request):
        serializer = EspacioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('espacios')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Vista para actualizar datos de un espacio    
class EspacioDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail_espacio.html'
    style = {'template_pack': 'rest_framework/horizontal/'}

    def get(self, request, pk):
        espacio = get_object_or_404(Espacio, pk=pk)
        serializer_spc = EspacioSerializer(espacio)
        serializer_prod = ProductoSerializer()
        query_prod_list = Producto.objects.filter(espacio_id = pk)
        return Response({'serializer_spc': serializer_spc, 'serializer_prod': serializer_prod, 'espacio': espacio, 'product_list': query_prod_list, 'style': self.style})

    def post(self, request, pk):
        espacio = get_object_or_404(Espacio, pk=pk)
        serializer = EspacioSerializer(espacio, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'espacio': espacio})
        serializer.save()
        return redirect('espacios')

#Vista para la opcion "ver" de un espacio    
class EspacioVer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ver_espacio.html'

    def get(self, request, pk):
        espacio = get_object_or_404(Espacio, pk=pk)
        query_prod_list = Producto.objects.all()
        serializer = EspacioSerializer(espacio)
        return Response({'serializer': serializer, 'espacio': espacio, 'product_list': query_prod_list})


#Vista por defecto de productos
class ProductoIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index_producto.html'

    def get(self, request):
            espacios = Espacio.objects.all()
            current_espacio = Espacio.objects.first()
            prod_espacio = Producto.objects.filter(espacio_id = current_espacio.id)
            prod_total = Producto.objects.all()

            return Response({'prod_list_total': prod_total, 'prod_list_espacio' : prod_espacio, 'current_espacio': current_espacio, 'espacios': espacios})

    def delete(request, pk, id):
        producto = Producto.objects.get(pk = pk)
        producto.delete()
        return redirect ('/productos/%d' %id)


#Vista de productos de un espacio en especifico
class ProductoEspIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index_producto.html'

    def get(self, request, pk):
            espacios = Espacio.objects.all()
            current_espacio = Espacio.objects.get(pk = pk)
            prod_espacio = Producto.objects.filter(espacio_id = pk)
            prod_total = Producto.objects.all()

            return Response({'prod_list_total': prod_total, 'prod_list_espacio' : prod_espacio, 'current_espacio': current_espacio, 'espacios': espacios})


#Vista para crear productos    
class ProductoCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'crear_producto.html'
    style = {'template_pack': 'rest_framework/horizontal/'}

    def get(self, request, pk):
        espacios = Espacio.objects.all()
        espacio = get_object_or_404(Espacio, pk=pk)
        prod_espacio = Producto.objects.filter(espacio_id = pk)
        prod_total = Producto.objects.all()
        serializer_prod = ProductoSerializer()

        return Response({'prod_list_total': prod_total, 'prod_list_espacio' : prod_espacio, 'espacio': espacio, 'espacios': espacios, 'serializer_prod': serializer_prod, 'style': self.style})

    def post(self, request, pk):  
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/productos/productosCreate/%d' %pk)
        print(serializer.errors)
        return redirect ('/productos/productosCreate/%d' %pk, {'mensaje': serializer.errors})
    
    def delete(request, pk, id):
        producto = Producto.objects.get(pk = pk)
        producto.delete()
        return redirect ('/productos/productosCreate/%d' %id)
    
class ProductoDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail_producto.html'
    style = {'template_pack': 'rest_framework/horizontal/'}

    def get(self, request, pk, id):
        espacios = Espacio.objects.all()
        espacio = get_object_or_404(Espacio, pk=id)
        producto = get_object_or_404(Producto, pk = pk)
        prod_espacio = Producto.objects.filter(espacio_id = id)
        prod_total = Producto.objects.all()
        serializer_prod = ProductoSerializer(producto)

        return Response({'prod_list_total': prod_total, 'prod_list_espacio' : prod_espacio, 'espacio': espacio, 'espacios': espacios, 'serializer_prod': serializer_prod, 'producto': producto,'style': self.style})

    def post(self, request, pk, id):  
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'producto': producto})
        serializer.save()
        return redirect('/productos/productosCreate/%d' %id, {'mensaje': serializer.errors})
    
    def delete(request, pk, id):
        producto = Producto.objects.get(pk = pk)
        producto.delete()
        return redirect ('/productos/productosCreate/%d' %id)

#Vista para crear una orden
class OrdenCreate(APIView):
    permission_classes = [permissions.AllowAny,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'crear_orden.html'

    def get(self, request):
        queryset = Producto.objects.all()
        return Response({'product_list': queryset})
    
    def post(self, request):

        codigo = request.POST.get('codigo')
        productos_ids = request.POST.getlist('productos')
        productos_ids_counter = Counter(productos_ids)
        
        orden = Orden.objects.create(codigo = codigo)
        productos = []
        for id in productos_ids:
            new_producto = {
                'orden': orden.id,
                'producto': id,
                'cantidad' : productos_ids_counter[id]
            }
            productos.append(new_producto)

        serializer = OrdenSerializer(data = {'codigo': codigo, 'productos': productos})
        
        if(serializer.is_valid()):
            serializer.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "order_notification_group",
            {
                "type": "notify_order_created",
            }
        )
    
        return redirect('ordenes')


#Vista para consultar ordenes por espacio
class OrdenesVer(APIView):
    permission_classes = [permissions.AllowAny,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'centro_ordenes.html'

    def get(self, request):
        queryset = Espacio.objects.all()
        return Response({'espacios': queryset})
    
class OrdenesDetail(APIView):
    permission_classes = [permissions.AllowAny,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orden_espacio.html'

    def get(self, request, pk):
        espacio = get_object_or_404(Espacio, pk=pk)
        productos = Producto.objects.filter(espacio_id = pk)
        ordenesProductos = OrdenProducto.objects.filter(producto__in=productos.values_list('id')).values('cantidad', 'orden_id', 'producto_id').distinct()
        ordenes = Orden.objects.filter(id__in = ordenesProductos.values_list('orden')).order_by('date')

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"orden_producto_updates_{pk}",
            {
                "type": "send_update",
                "message": {
                    'espacio': espacio,
                    'ordenes': ordenes,
                    'productos': productos,
                    'ordenesProductos': ordenesProductos,
                },
            },
        )


        return Response({'espacio': espacio, 'ordenes': ordenes, 'productos': productos, 'ordenesProductos': ordenesProductos})

    def delete(request, id, pk):
        orden = Orden.objects.get(pk = pk)
        productos = Producto.objects.filter(espacio_id = id)
        ordenesProductos = OrdenProducto.objects.filter(Q(orden_id = pk, producto__in = productos.values_list('id')))
    
        for ordenProducto in ordenesProductos:
            ordenProducto.delete()
        
        if(not (OrdenProducto.objects.filter(orden__id = pk))):
            orden.delete()
    
        return redirect ('/ordenesCentro/%d' %id)

class MesaIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index_mesas.html'

    def get(self, request):
        mesas = Mesa.objects.all()
        return Response({'mesas': mesas})

    def delete(request, pk):
        mesa = Mesa.objects.get(pk = pk)
        mesa.delete()
        return redirect('mesas')

class MesaCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'crear_mesa.html'

    def get(self, request):
        serializer = MesaSerializer()

        return Response({'serializer': serializer})

    def post(self, request):
        serializer = MesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('mesas')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MesaDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail_mesa.html'
    

    def get(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        serializer_mesa = MesaSerializer(mesa)
    
        return Response({'serializer_mesa': serializer_mesa})

    def post(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        serializer = MesaSerializer(mesa, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('mesas')

class MesaView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ver_mesa.html'

    def get(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        serializer = MesaSerializer(mesa)
        return Response({'serializer': serializer})