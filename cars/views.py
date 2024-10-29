from django.shortcuts import render, redirect
from cars.models import Car, Marca
from cars.forms import CarroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def home(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(modelo__icontains=search)

    return render(request, 'home.html', {'title': 'home',
                                         'id': 'home',
                                         'cars': cars})


def cadastro_veiculos(request):
    new_car = CarroForm()
    if request.method == 'POST':
        new_car = CarroForm(request.POST, request.FILES)
        if new_car.is_valid():
            new_car.save()
            return redirect('home')
    return render(request, 'cadastro_veiculo.html', {'title': 'cadastre seu veiculo', 'id': 'register', 'form': new_car})


def loginView(request):
    if (request.method == 'POST'):

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'id': 'login'})


def logoutView(request):
    logout(request)
    return redirect('home')


def car(request, id):
    car = Car.objects.get(pk=id)
    return render(request, 'car.html', {'title': 'car', 'id': 'car', 'car': car})


def criar_conta(request):
    user_form = UserCreationForm()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    return render(request, 'criar_conta.html', {'title': 'crie sua conta', 'id': 'account', 'form': user_form})
