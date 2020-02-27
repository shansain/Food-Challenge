from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from .forms import SignUpClientForm, SignUpBusinessForm
from .models import Challenge, Client, Business, UserInChallenge


def home(request):
    c = Challenge.objects.all().order_by('?')
    d = {'object_list': c}
    return render(request, 'core/home.html', d)


# @login_required
def search(request):
    q = request.GET.get('q')
    c = Challenge.objects.filter(Q(name__icontains=q) | Q(summary__icontains=q) | Q(description__icontains=q))
    for n in c:
        if request.user.is_authenticated:
            n.in_challenge = UserInChallenge.objects.filter(
                client=request.user.client,
                challenge_id=n.id
            ).exists()

    context = {'object_list': c}
    return render(request, 'core/search.html', context)


# @login_required
def select(request, challenge_id):
    c = Challenge.objects.get(id=challenge_id)
    in_challenge = False
    if request.user.is_authenticated:
        in_challenge = UserInChallenge.objects.filter(
            client=request.user.client,
            challenge_id=challenge_id
        ).exists()
    if request.method == 'POST':
        UserInChallenge.objects.create(
            client=request.user.client,
            challenge_id=challenge_id
        )
        in_challenge = True
    challenge_list = [
        "Chinese food challenge",
        "Vegan Instant",
        "Food Diggers",
        "Indian food challenge",
        "Special challenge for a limited time",
        "Jerusalem Challenge",
        "The Shawarma Challenge",
    ]
    context = {'object': c, 'in_challenge': in_challenge}
    return render(request, 'core/challenge_page.html', context)


class NoneLoginPermitted(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class SignUpClientView(NoneLoginPermitted, FormView):
    template_name = 'registration/signup_client.html'
    form_class = SignUpClientForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
        Client.objects.create(
            user=user,
        )
        login(self.request, user)
        return super(SignUpClientView, self).form_valid(form)


class SignUpBusinessView(FormView):
    template_name = 'registration/signup_business.html'
    form_class = SignUpBusinessForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
        business = Business.objects.create(
            user=user,

            location=data['location'],
            description=data['description'],
            start_hour=data['start_hour'],
            end_hour=data['end_hour']
        )
        business.days.set(data['days']),
        business.save()
        login(self.request, user)
        return super(SignUpBusinessView, self).form_valid(form)


def profile(request, client):
    challenge = UserInChallenge.objects.filter(client__user_id=client)
    return render(request, 'core/fixed_profile.html', {'client': Client.objects.get(user_id=client), 'challenge': challenge})


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')

    return render(request, 'home.html')
