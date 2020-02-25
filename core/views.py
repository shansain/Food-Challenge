from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from .forms import SignUpClientForm, SignUpBusinessForm
from .models import Challenge, Client, Business


def home(request):
    c = Challenge.objects.all().order_by('?')
    d = {'object_list': c}
    return render(request, 'core/home.html', d)


@login_required
def search(request):
    q = request.GET.get('q')
    c = Challenge.objects.filter(Q(name__icontains=q) | Q(summary__icontains=q) | Q(description__icontains=q))
    context = {'object_list': c}
    return render(request, 'core/search.html', context)


@login_required
def select(request, challenge_id):
    c = Challenge.objects.get(id=challenge_id)
    context = {'object': c}
    return render(request, 'core/challenge_page.html', context)


class NoneLoginPermitted(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class SignUpClientView(NoneLoginPermitted, FormView):
    template_name = 'registration/signup_client.html'
    form_class = SignUpClientForm
    success_url = reverse_lazy('core:search')

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
    success_url = reverse_lazy('core:search')

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
        # treatments_qs = TreatmentType.objects.filter(name__contains=data['treatments'])
        print(data['treatments'])
        business = Business.objects.create(
            user=user,
            phone=data['phone'],
            location=data['location'],
            description=data['description'],
            start_hour=data['start_hour'],
            end_hour=data['end_hour']
        )
        business.treatments.set(data['treatments']),
        business.days.set(data['days']),
        business.save()
        login(self.request, user)
        return super(SignUpBusinessView, self).form_valid(form)


def logout(request):
    auth.logout(request)
    return render(request, 'core/home.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')

    return render(request, 'home.html')
