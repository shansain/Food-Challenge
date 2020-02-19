from django.db.models import Q
from django.shortcuts import render
from .models import Challenge


def home(request):
    c = Challenge.objects.all().order_by('?')
    d = {'object_list': c}
    return render(request, 'core/home.html', d)


def search(request):
    q = request.GET.get('q')
    c = Challenge.objects.filter(Q(name__icontains=q) | Q(summary__icontains=q) | Q(description__icontains=q))
    context = {'object_list': c}
    return render(request, 'core/search.html', context)


def select(request, challenge_id):
    c = Challenge.objects.get(id=challenge_id)
    context = {'object': c}
    return render(request, 'core/challenge_page.html', context)
