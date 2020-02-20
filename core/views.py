from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import SignUpForm
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


def signup(request):
    print(request.user.username)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data['username'],
                email=data['email']
            )
            user.set_password(data['password'])
            user.save()
            login(request, user)
    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request, 'core/home.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')

    return render(request, 'home.html')
