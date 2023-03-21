from django.shortcuts import render
from .forms import FormLinks


def home(request):
    form = FormLinks()
    return render(request, 'home.html', {'form': form})
