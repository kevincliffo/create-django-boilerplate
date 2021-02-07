import os
from django.shortcuts import render, redirect

def index(request):
    context = {}
    return render(request, 'template/index.html', context)