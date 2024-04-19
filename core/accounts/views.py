from django.shortcuts import render
from django.views.generic import CreateView
from .models import User

class Sign_Up(CreateView):
    model = User
    fields = ['email','password']
    success_url = '/accounts/login/'
    template_name = 'registration/sign_up.html'
    