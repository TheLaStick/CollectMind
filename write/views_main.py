from django.http import HttpResponse
from django.shortcuts import render, redirect
from write.models import CollectMind
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
text2 = ""
def main(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return redirect('/login')

def Login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            messages.error(request, 'Заполните все поля!')
            return redirect('/login')

        # проверяем правильность логина и пароля
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('/login')

def Register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        if username == '' or password == '' or email == '':
            return HttpResponse("Заполните все поля")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Логин занят")

        # создаем пользователя
        user = User.objects.create_user(username, email, password)
        user.save()

        # "входим" пользователя
        login(request, user)
        return redirect('/')

def KaboLogout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/login')

def write(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'GET':
        claims = CollectMind.objects.all()
        return render(request, 'write.html',{'claims' : claims})

    if request.method == 'POST':
        if request.POST.get('send') == 'Отправить продолжение':
            name = request.POST['name']
            text = request.POST['text']

            tale.name = name
            tale.text = tale.text + text
            tale.author = request.user
            tale.end = False
            tale.save()
            return redirect( '/writelate')
        if request.POST.get('end') == 'Закончить рассказ...':
            name = request.POST['name']
            tale = CollectMind()
            tale.name = name
            tale.text = tale.text
            tale.author = request.user
            tale.end = True
            tale.save()
            return redirect('/ended')

def read(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    claims = CollectMind.objects.all()
    return render(request, 'read.html', { 'claims' : claims })

def writelate(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'write_late.html')

def ended(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'ended.html')


