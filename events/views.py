from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
        return render(request,'events/index.html')
