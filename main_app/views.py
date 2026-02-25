from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Jellycat, Accessory
from .forms import FeedingForm


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def jellycat_index(request):
   
    jellycats = jellycat.objects.filter(user=request.user)
    return render(request, 'jellycats/index.html', {'jellycats': jellycats})

@login_required
def jellycat_detail(request, jellycat_id):
    jellycat_instance = jellycat.objects.get(id=jellycat_id)
    accessories_jellycat_doesnt_have = accessory.objects.exclude(id__in = jellycat_instance.accessories.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'jellycats/detail.html', {
        'jellycat': jellycat_instance,
        'accessories': accessories_jellycat_doesnt_have
        })

class JellycatCreate(LoginRequiredMixin, CreateView):
    model = jellycat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/jellycats/'

class JellycatUpdate(LoginRequiredMixin, UpdateView):
    model = jellycat    
    fields = ['type', 'description', 'age']

class JellycatDelete(LoginRequiredMixin, DeleteView):
    model = jellycat
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
    jellycat.objects.get(id=jellycat_id).accessories.add(accessory_id)
    return redirect('jellycat-detail', jellycat_id=jellycat_id)

@login_required
def remove_accessory(request, jellycat_id, accessory_id):
    jellycat_instance = jellycat.objects.get(id=jellycat_id)
    accessory_instance = accessory.objects.get(id=accessory_id)
    jellycat_instance.accessories.remove(accessory_instance)
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
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    