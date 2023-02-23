from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'form':form
    }
    template = loader.get_template('sign_up.html')
    return HttpResponse(template.render(context, request))