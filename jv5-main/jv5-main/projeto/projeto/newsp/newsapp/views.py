from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image 
import os
from django.conf import settings
from datetime import date 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "pagina1.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        
        img = Image.open(file)
        path = os.path.join(settings.BASE_DIR, f'media/{file.name}-{date.today()}.png')
        img = img.save(path)


        print(file)

        return HttpResponse('concluido')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ja existe um usuario com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('cadastrado com sucesso!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)

    if user:
        login_django(request, user)

        return HttpResponse('concluido')
    else:
        return HttpResponse('autenticação falhou. login ou senha inválidos.')

 
def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('Plataforma')
    return HttpResponse('voce precisa estar logado')

