from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from espacios import views

urlpatterns = [
    path('espacios/', views.EspacioIndex.as_view(), name='espacios'),

    path('espacios/<int:pk>/', views.EspacioIndex.delete, name='borrar_espacio'),
    path('espacios/crearEspacio/', views.EspacioCreate.as_view(), name= 'crear_espacio'),
    path('espacios/espacioDetail/<int:pk>/', views.EspacioDetail.as_view(), name= 'detail_espacio'),
    path('espacios/espacioVer/<int:pk>/', views.EspacioVer.as_view(), name= 'ver_espacio'),
    path('espacios/addProducto/<int:pk>', views.ProductoDetail.as_view(), name= 'add_producto'),
    path('espacios/espacioDetail/<int:pk>/<int:id>', views.ProductoDetail.delete, name= 'borrar_producto'),

    path('ordenes/', views.OrdenCreate.as_view(), name= 'ordenes'),
    path('ordenesCentro/', views.OrdenesVer.as_view(), name='ver_ordenes'),
    path('ordenesCentro/<int:pk>/', views.OrdenesDetail.as_view(), name='orden_detail'),
    path('ordenesCentro/<int:id>/<int:pk>', views.OrdenesDetail.delete, name= 'borrar_orden'),
]

urlpatterns = format_suffix_patterns(urlpatterns)