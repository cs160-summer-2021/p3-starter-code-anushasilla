from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')


def landing(request):
    return render(request, 'coloring/landing.html')

def triangle(request):
    return render(request, 'coloring/triangle.html')

def flowers(request):
    return render(request, 'coloring/flowers.html')
    
def blank(request):
    return render(request, 'coloring/blank.html')

