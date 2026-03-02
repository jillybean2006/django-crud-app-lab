from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Jellycat, Accessory
from .forms import AccessoryForm


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


@login_required
def jellycat_index(request):
    jellycats = Jellycat.objects.filter(user=request.user)
    return render(request, 'jellycats/index.html', {'jellycats': jellycats})


@login_required
def jellycat_detail(request, jellycat_id):
    jellycat = Jellycat.objects.get(id=jellycat_id)

    # accessories the jellycat DOESN'T have yet
    accessories_jellycat_doesnt_have = Accessory.objects.exclude(
        id__in=jellycat.accessories.all().values_list('id', flat=True)
    )

    accessory_form = AccessoryForm()

    return render(request, 'jellycats/detail.html', {
        'jellycat': jellycat,
        'accessories': accessories_jellycat_doesnt_have,
        'accessory_form': accessory_form,
    })


class JellycatCreate(LoginRequiredMixin, CreateView):
    model = Jellycat
    fields = ['name', 'type', 'description', 'age']
    success_url = '/jellycats/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JellycatUpdate(LoginRequiredMixin, UpdateView):
    model = Jellycat
    fields = ['type', 'description', 'age']


class JellycatDelete(LoginRequiredMixin, DeleteView):
    model = Jellycat
    success_url = '/jellycats/'


class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = '__all__'


class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory


class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory


class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['name', 'color']


class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = '/accessories/'


@login_required
def associate_accessory(request, jellycat_id, accessory_id):
    Jellycat.objects.get(id=jellycat_id).accessories.add(accessory_id)
    return redirect('jellycat-detail', jellycat_id=jellycat_id)


@login_required
def remove_accessory(request, jellycat_id, accessory_id):
    jellycat = Jellycat.objects.get(id=jellycat_id)
    jellycat.accessories.remove(accessory_id)
    return redirect('jellycat-detail', jellycat_id=jellycat_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('jellycat-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })