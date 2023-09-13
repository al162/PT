from espacios.models import Espacio, Producto
from espacios.serializers import EspacioSerializer, ProductoSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

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

#Vista para ver productos
class ProductoView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'crear_orden.html'

    def get(self, request):
        queryset = Producto.objects.all()
        return Response({'product_list': queryset})

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
