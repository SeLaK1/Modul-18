from django.shortcuts import render

# Create your views here.

def platform(request):
    title = 'мой сайт'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    contex = {
        'Title': 'Каталог игр',
        'game1': 'Minecraft',
        'game2': 'KS2',
        'game3': 'Star Craft',
    }
    return render(request, 'third_task/games.html', contex)

def cart(request):
    return render(request, 'third_task/cart.html')