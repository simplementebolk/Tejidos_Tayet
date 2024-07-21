from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('acceso_denegado/', acceso_denegado, name='acceso_denegado'),
    path('productos/', productos, name="productos"),
    path('producto/<int:producto_id>/', producto_detalle, name='producto_detalle'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/', carrito_detalle, name='carrito_detalle'),
    path('decrementar-cantidad/<int:item_id>/', decrementar_cantidad, name='decrementar_cantidad'),
    path('incrementar-cantidad/<int:item_id>/', incrementar_cantidad, name='incrementar_cantidad'),
    path('pago/', pago , name="pago"),
]