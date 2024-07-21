from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .webpay_config import tx
import time

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def contacto(request):
    return render(request, 'core/contacto.html')

#LISTAR PRODUCTOS
def productos(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')
    search_query = request.GET.get('search', '')

    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    if search_query:
        productos = productos.filter(nombre__icontains=search_query) | productos.filter(descripcion__icontains=search_query)

    return render(request, 'core/productos.html', {'productos': productos, 'categorias': categorias})

def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'core/producto_detalle.html', {'producto': producto})


def acceso_denegado(request):
    return render(request, 'core/acceso_denegado.html')

#LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('index')
        else:
            messages.error(request, 'Error en el inicio de sesión. Por favor verifica tus credenciales.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})


#CARRITO

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item = Carrito.objects.filter(usuario=request.user, producto=producto).first()

    if carrito_item:
        if carrito_item.cantidad < producto.stock:
            carrito_item.cantidad += 1
            carrito_item.save()
            messages.success(request, "Producto añadido al carrito.")
        else:
            messages.error(request, "No hay suficiente stock disponible.")
    else:
        if producto.stock > 0:
            Carrito.objects.create(usuario=request.user, producto=producto)
            messages.success(request, "Producto añadido al carrito.")
        else:
            messages.error(request, "No hay suficiente stock disponible.")

    return redirect("carrito_detalle")

@login_required
def eliminar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(Carrito, id=item_id)

    if carrito_item.usuario == request.user:
        carrito_item.delete()
        messages.success(request, "Producto eliminado del carrito.")

    return redirect("carrito_detalle")

@login_required
def vaciar_carrito(request):
    Carrito.objects.filter(usuario=request.user).delete()
    return render(request, "core/carrito.html")

@login_required
def carrito_detalle(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total_precio = sum(item.get_total_precio() for item in carrito_items)

    context = {
        "carrito_items": carrito_items,
        "total_precio": total_precio,
    }

    return render(request, "core/carrito.html", context)

@login_required
def incrementar_cantidad(request, item_id):
    carrito_item = get_object_or_404(Carrito, id=item_id)
    if carrito_item.usuario == request.user:
        if carrito_item.cantidad < carrito_item.producto.stock:
            carrito_item.cantidad += 1
            carrito_item.save()
            messages.success(request, "Cantidad incrementada.")
        else:
            messages.error(request, "No hay suficiente stock disponible.")
    return redirect('carrito_detalle')


@login_required
def decrementar_cantidad(request, item_id):
    carrito_item = get_object_or_404(Carrito, id=item_id)
    if carrito_item.usuario == request.user and carrito_item.cantidad > 1:
        carrito_item.cantidad -= 1
        carrito_item.save()
        messages.success(request, "Cantidad decrementada.")
    return redirect('carrito_detalle')

@login_required
def pago(request):
    return render(request, 'core/pago.html')

#PAGO

@login_required
def iniciar_pago(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    if not carrito_items.exists():
        return redirect('carrito_detalle')

    total_precio = sum(item.get_total_precio() for item in carrito_items)
    buy_order = f'{request.user.id}-{int(time.time())}'
    session_id = request.session.session_key
    return_url = request.build_absolute_uri(reverse('confirmar_pago'))

    try:
        response = tx.create(buy_order, session_id, total_precio, return_url)
        request.session['token'] = response['token']
        return redirect(response['url'] + '?token_ws=' + response['token'])
    except WebpayException as e:
        return render(request, 'core/error_pago.html', {'error': str(e)})

@login_required
def confirmar_pago(request):
    token = request.GET.get('token_ws')
    try:
        response = tx.commit(token)
        if response['status'] == 'FAILED':
            error_message = response.get('detail', 'Error desconocido')
            return render(request, 'core/error_pago.html', {'error': error_message})
        carrito_items = Carrito.objects.filter(usuario=request.user)
        for item in carrito_items:
            producto = item.producto
            producto.stock -= item.cantidad
            producto.save()

        carrito_items.delete()
        return render(request, 'core/exito_pago.html', {'response': response})
    except:
        return render(request, 'core/error_pago.html',)
