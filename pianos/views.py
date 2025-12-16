from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from pianos.models.pianos import Piano


def list(request):
    pianos = Piano.objects.all()
    return render(request, 'pianos/list.html', {'pianos': pianos})


class PianoListView(ListView):
    model = Piano
    context_object_name = 'pianos'


def details(request, pk):
    piano = get_object_or_404(
        Piano.objects, pk=pk
    )
    return render(request, 'pianos/details.html', {'piano': piano})


class PianoDetailView(DetailView):
    model = Piano
    context_object_name = 'piano'


def create(request):
    # pianos = Piano.objects.all()
    return render(request, 'pianos/create.html')
