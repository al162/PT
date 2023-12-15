from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from espacios import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),

    path('espacios/', views.EspacioIndex.as_view(), name='espacios'),

    path('espacios/<int:pk>/', views.EspacioIndex.delete, name='borrar_espacio'),
    path('espacios/crearEspacio/', views.EspacioCreate.as_view(), name= 'crear_espacio'),
    path('espacios/espacioDetail/<int:pk>/', views.EspacioDetail.as_view(), name= 'detail_espacio'),
    path('espacios/espacioVer/<int:pk>/', views.EspacioVer.as_view(), name= 'ver_espacio'),
    
    path('mesas/', views.MesaIndex.as_view(), name='mesas'),
    path('mesas/crearMesa/', views.MesaCreate.as_view(), name='crear_mesa'),
    path('mesas/<int:pk>', views.MesaIndex.delete, name="borrar_mesa"),
    path('mesas/mesaDetail/<int:pk>/', views.MesaDetail.as_view(), name= 'detail_mesa'),
    path('mesas/mesaVer/<int:pk>/', views.MesaView.as_view(), name="ver_mesa"),

    path('productos/', views.ProductoIndex.as_view(), name = 'productos'),

    path('productos/<int:pk>/', views.ProductoEspIndex.as_view(), name='productos_esp'),
    path('productos/<int:pk>/<int:id>', views.ProductoIndex.delete, name='borrar_producto'),

    path('productos/productosCreate/<int:pk>/', views.ProductoCreate.as_view(), name='crear_producto'),
    path('productos/productosCreate/<int:pk>/<int:id>', views.ProductoCreate.delete, name='borrar_producto_crear'),

    path('productos/productosDetail/<int:pk>/<int:id>', views.ProductoDetail.as_view(), name='detail_producto'),

    path('ordenes/', views.OrdenCreate.as_view(), name= 'ordenes'),

    path('ordenesCentro/', views.OrdenesVer.as_view(), name='ver_ordenes'),
    path('ordenesCentro/<int:pk>/', views.OrdenesDetail.as_view(), name='orden_detail'),
    path('ordenesCentro/<int:id>/<int:pk>', views.OrdenesDetail.delete, name= 'borrar_orden'),
]

urlpatterns = format_suffix_patterns(urlpatterns)