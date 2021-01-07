from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProfileCreationForm, SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.
from .models import Contact


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')


class CreateContact(CreateView):
    model = Contact
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home:home')
    fields = '__all__'


def contact(request):
    return render(request, 'home/contact.html')


def signup(request):
    form = SignUpForm()
    form2 = ProfileCreationForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)

    return render(request, 'home/signup.html', {'form': form, 'form2': form2})


