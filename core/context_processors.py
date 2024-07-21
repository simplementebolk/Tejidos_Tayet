from .models import Carrito
from django.db.models import Sum

def carrito_context(request):
    if request.user.is_authenticated:
        cantidad_total = Carrito.objects.filter(usuario=request.user).aggregate(total_cantidad=Sum('cantidad'))['total_cantidad'] or 0
    else:
        cantidad_total = 0
    return {'cantidad_total': cantidad_total}
