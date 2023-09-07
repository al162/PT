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
]

urlpatterns = format_suffix_patterns(urlpatterns)