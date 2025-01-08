from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

def sign_up_by_html(request):
    users = ['Andrey', 'Igor', 'Sergey']
    info = {'error': None}
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        second_password = request.POST.get('second_password')
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Возраст не менее 18'
        elif password != second_password:
            info['error'] = 'Пароли не совпадают'
        elif login in users:
            info['error'] = 'Данный пользователь уже существует'
        else:
            users.append(login)
            return HttpResponse(f'Приветствуем, {login}')
    context = {
        'info': info['error']
    }
    return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_django(request):
    users = ['Andrey', 'Igor', 'Sergey']
    info = {'error': None}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            second_password = form.cleaned_data['second_password']
            age = form.cleaned_data['age']

            if int(age) < 18:
                info['error'] = 'Возраст не менее 18'
            elif password != second_password:
                info['error'] = 'Пароли не совпадают'
            elif login in users:
                info['error'] = 'Данный пользователь уже существует'
            else:
                users.append(login)
                return HttpResponse(f'Приветствуем, {login}')
    else:
        form = UserRegister()
    context = {
        'form': form,
        'info': info['error']
    }
    return render(request, 'fifth_task/registration_page.html', context)














