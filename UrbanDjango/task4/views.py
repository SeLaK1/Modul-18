from django.shortcuts import render

# Create your views here.

def platform(request):
    title = 'мой сайт'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/platform.html', context)

def games(request):
    contex = {'game1': 'Atomic Heart',
              'game2': "Cyberpunk 2077",
              'game3': 'Minecraft',
              'games': ['Atomic Heart', "Cyberpunk 2077", 'Minecraft']}
    return render(request, 'fourth_task/games.html', contex)

def cart(request):
    return render(request, 'fourth_task/cart.html')

def menu(request):
    return render(request, 'fourth_task/menu.html')