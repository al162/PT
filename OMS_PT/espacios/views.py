from collections import Counter
from espacios.models import Espacio, Producto, Orden, OrdenProducto
from espacios.serializers import EspacioSerializer, ProductoSerializer, OrdenSerializer, OrdenProductoSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#Vista para el indice de espacios
class EspacioIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index_espacio.html'

    def get(self, request):
        queryset = Espacio.objects.all()
        return Response({'espacios': queryset})
    
    def delete(request, pk):
        espacio = Espacio.objects.get(pk = pk)
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
        query_prod_list = Producto.objects.all()
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

#Vista para actualizar datos de un producto    
class ProductoDetail(APIView):
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        query = Producto.objects.all()
        return Response({'serializer': query})

    def post(self, request, pk):  
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/espacios/espacioDetail/%d' %pk)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(request, pk, id):
        producto = Producto.objects.get(pk = pk)
        producto.delete()
        return redirect ('/espacios/espacioDetail/%d' %id)

#Vista para crear una orden
class OrdenCreate(APIView):
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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'centro_ordenes.html'

    def get(self, request):
        queryset = Espacio.objects.all()
        return Response({'espacios': queryset})
    
class OrdenesDetail(APIView):
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

