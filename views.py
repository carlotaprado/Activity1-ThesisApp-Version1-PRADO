# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Thesis

def thesis_list(request):
    thesis_list = Thesis.objects.all()
    return render(request, 'thesis/thesis_list.html', {'thesis_list': thesis_list})

def thesis_add(request):
    # Your logic for adding a thesis goes here
    return HttpResponse("Add thesis view")
