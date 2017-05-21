from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('No ninjas here')

def ninjas(request):
    context = {
        'src': '/disappearingNinjas_app/images/tmnt.png'
    }
    return render(request, 'disappearingNinjas_app/index.html', context)

def color(request, color):
    # context dict holds notapril.jpg by default if none of the colors match url
    context = {'src': '/disappearingNinjas_app/images/notapril.jpg'}
    ninja_color = {
        'blue': '/disappearingNinjas_app/images/leonardo.jpg',
        'orange': '/disappearingNinjas_app/images/michelangelo.jpg',
        'red': '/disappearingNinjas_app/images/raphael.jpg',
        'purple': '/disappearingNinjas_app/images/donatello.jpg'
    }
    # if color matches any of the key names, overwrite context's value to src location
    if color in ninja_color:
        context['src'] = ninja_color[color]
    return render(request, 'disappearingNinjas_app/index.html', context)
