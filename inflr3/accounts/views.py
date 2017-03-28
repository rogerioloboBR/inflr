from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.http import HttpResponseRedirect
# Create your views here.

# def login(request):
#     return (request,'accounts/login.html')


def register(request):
    template_name = 'accounts/add_user.html'
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request,template_name,context)
