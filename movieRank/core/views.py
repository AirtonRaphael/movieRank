from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.models import User

class Index(View):
    def get(self, request):
        return render(request, 'core/index.html')


class Login(View):
    def get(self, request):
        data = {'error' : ''}
        return render(request, 'core/login.html', data)

    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        if email == '' or senha == '':
            data = {'error': 'Por favor preencha todos os campos.'}
            return render(request, 'core/login.html', data)

        try:
            user = User.objects.get(email=email)

            if user.password == senha:
                return render(request, 'core/lista.html')

            data = {'error': 'Email ou senha incorretos.'}
            return render(request, 'core/login.html', data)
        except Exception as error:
            data = {'error':'Erro inesperado, por favor entre em contato com o desenvolvedor.'}
            return render(request, 'core/login.html', data)

class Register(View):
    def get(self, request):
        data = {'error': 'aqui'}
        return render(request, 'core/register.html', data)
    
    def post(self, request):
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username == '' or email == '' or password == '':
            data = {'error': 'Por favor preencha todos os campos.'}
            return render(request, 'core/register.html', data)

        user_check= User.objects.filter(username=username)
        email_check = User.objects.filter(email=email)

        if user_check == 0:
            data = {'error': 'Usuário já existe.'}
            return render(request, 'core/register.html', data)
        elif email_check == 0:
            data = {'error': 'Email cadastrado.'}
            return render(request, 'core/register.html', data)

        try:
            user = User(username=username, email=email, password=password)
            user.save()
            return HttpResponseRedirect('login')
        except Exception as error:
            data = {'error': 'Erro inesperado, por favor entre em contato com o desenvolvedor.'}
            return render(request, 'core/register.html', data)