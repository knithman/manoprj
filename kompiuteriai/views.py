from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from django.db.models import Q

from .models import Kompiuteris, Stacionarus, Nesiojamas

def index(request):
    num_kompiuteriai = Kompiuteris.objects.all().count()
    num_stacionarus = Stacionarus.objects.count()
    num_nesiojami = Nesiojamas.objects.count()

    context_t = {
        'num_kompiuteriai_t': num_kompiuteriai,
        'num_stacionarus_t': num_stacionarus,
        'num_nesiojami_t': num_nesiojami,
    }

    return render(request, 'index.html', context=context_t)

def kompiuteriai(request):
    kompiuteriai_visos_eilutes = Kompiuteris.objects.all()
    context_t = {
        'kompiuteriai_visos_eilutes_t': kompiuteriai_visos_eilutes
    }
    return render(request, 'kompiuteriai_visi.html', context=context_t)


def kompiuteris(request, kompiuteris_id):
    kompiuteris_viena_eilute = get_object_or_404(Kompiuteris, pk=kompiuteris_id)
    context_t = {
        'kompiuteris_viena_eilute_t': kompiuteris_viena_eilute
    }
    return render(request, 'kompiuteris_vienas.html', context=context_t)

class KompiuterisListView(generic.ListView):
    model = Kompiuteris
    context_object_name = 'kompiuteris_list'
    template_name = 'kompiuteriai_visi.html'

class KompiuterisDetailView(generic.DetailView):
    model = Kompiuteris
    context_object_name = 'kompiuteris'
    template_name = 'kompiuteris_vienas.html'

# paieškos viewsas
def search_stacionarus(request):
    paieskos_tekstas = request.GET.get('laukelio-tekstas')
    paieskos_rezultatai = Stacionarus.objects.filter(
        Q(kompiuteris__icontains=paieskos_tekstas) |
        Q(aprasymas__icontains=paieskos_tekstas)
    )

    context = {
        'paieskos_tekstas_t': paieskos_tekstas,
        'paieskos_rezultatai_t': paieskos_rezultatai
    }
    return render(request, 'paieskos-rezultatai.html', context=context)