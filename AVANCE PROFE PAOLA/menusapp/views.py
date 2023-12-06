from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Cliente, Administrador, Menu
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm 
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseForbidden


def index(request):
    return render(request, 'logins/index.html')



def register(request):
    if request.method == 'POST':
        
        rut = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')

        
        if password == re_password:
          
           

          
            user = User.objects.create(
                username=rut,
                first_name=nombre,
                last_name=last_name,
                email=email,
                password=make_password(password) 
            )

          
            cliente = Cliente.objects.create(
                usuario=user,
                nombre=nombre
            )

           
            login(request, user)
            return redirect('/login')
        else:
            
            pass

   
    return render(request, 'logins/register.html')

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'logins/login.html', {'error_message': 'Credenciales incorrectas'})
    return render(request, 'logins/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='inicio')
def dashboard(request):
    users = User.objects.all()
    data = {'users':users}
    return render(request, 'logins/dashboard.html', data)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nombre = request.POST.get('nombre')
        is_admin = request.POST.get('is_admin') == 'on'

       
        user = User.objects.create(
            username=username,
            password=make_password(password),
            first_name=nombre,
            is_superuser=is_admin,
            is_staff=is_admin  
        )

        
        if is_admin:
            Administrador.objects.create(usuario=user, nombre=nombre)

       
        return redirect('/')
    else:
        
        return render(request, 'web/crear_usuario.html')
    


@login_required
@user_passes_test(lambda u: u.is_superuser)
def crear_menu(request):
    if not request.user.is_superuser:
      
        return HttpResponseForbidden("No tienes permisos para ver esta página.")
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

    
        menu = Menu(nombre=nombre, descripcion=descripcion, precio=precio)
        menu.save()

       
        return redirect('/')
    else:
        
        return render(request, 'web/crear_menu.html')

@login_required    
def listar_menu(request):
    
    menus = Menu.objects.all()
   
    context = {'menus': menus}
    return render(request, 'web/listar_menu.html', context)