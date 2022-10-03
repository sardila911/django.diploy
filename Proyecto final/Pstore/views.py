import re
from django.shortcuts import render 
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from django.contrib.auth.models import User

from .forms import RegisterForm




def contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['jmjcables123@gmail.com']
        )
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'contacto.html',{

    })
	 



def index(request):
    return render(request, 'index.html',{
        #Contexto
    })
    
def catalogo(request):
    return render(request, 'catalogo.html',{
       
    })
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('pagina principal')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
        
    
    return render(request, 'users/login.html', {
        
    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')



    
def register(request):
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')   
        
        
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado con éxito!')
            return redirect('pagina principal')
    
    return render(request, 'users/register.html',{
       'form': form
    })


def catalogo(request):
    return render(request, 'catalogo.html', {
        
    })