from django.shortcuts import render


def main_page(request):
    return render(request, 'main.html')


def sight_page(request):
    return render(request, 'sight.html')