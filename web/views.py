from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Pagina incial.
def home(request):
    return render(request,'home.html')

#Pagina de cadastro
def create(request):
    return render(request,'create.html')

#Pagina de store
@csrf_exempt
def teste(request):
    return JsonResponse({'alo': 'opa'})
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmarção de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuario cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html', data)

# Pagina painel do login.
def painel(request):
    return render(request,'painel.html')

# Procesa o login.
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou Senha invaidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html', data)

# Pagina inicial do dashboard.
def dashboard(request):
    return render(request,'dashboard/home.html')

# Logout do sistema
def logouts(request):
    logouts(request)
    return redirect('/painel/')

#alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')