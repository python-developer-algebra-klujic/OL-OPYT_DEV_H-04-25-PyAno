from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from chords.models.chords import Chord


def list(request):
    chords = Chord.objects.all()
    return render(request, 'chords/list.html', {'chords': chords})


class ChordListView(ListView):
    model = Chord
    context_object_name = 'chords'


def details(request, pk):
    chord = get_object_or_404(
        Chord.objects, pk=pk
    )
    return render(request, 'chords/details.html', {'chord': chord})


class ChordDetailView(DetailView):
    model = Chord
    context_object_name = 'chord'



def create(request):
    # chords = Chord.objects.all()
    return render(request, 'chords/create.html')


class ChordCreateView(CreateView):
    model = Chord
    fields = '__all__'

    success_url = reverse_lazy('chords:chords_list')
