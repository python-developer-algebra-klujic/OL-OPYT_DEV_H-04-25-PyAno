from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'pianos/list.html')


def details(request):
    return render(request, 'pianos/details.html')
