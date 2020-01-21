from django.shortcuts import render
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.db.models import Q

from .custom_forms import *

User = get_user_model()


def login_view(request):
    context = {}
    register_form = UserRegisterForm(request.POST or None)
    login_form    = UserLoginForm(request.POST or None)
    context['register_form'] = register_form
    context['login_form']    = login_form
    if login_form.is_valid():
        query    = login_form.cleaned_data.get('query', '')
        password = login_form.cleaned_data.get('password', '')

        user = User.objects.filter(
            Q(username__iexact=query)|
            Q(email__iexact=query)
        ).distinct()

        if not user.exists() and user.count() != 1:   
            login_message = _('This user does not exist')
        user = user.first()

        if not user.check_password(password):
            login_message = _('Incorrect password')
            context['login_message'] = login_message
            return render(request, 'auth.html', context)

        # if not user.is_active:
        #     login_message = _('This user is not active')
        #     context['login_message'] = login_message
        #     return render(request, 'auth.html', context)
            
        # authenticate(username=user.username, password=password)
        login(request, user)
        # next = request.GET.get('next')
        # if next:
        #     return redirect(next)
        return redirect('home')
    return render(request, "auth.html", context)


def register_view(request):
    context = {}
    register_form = UserRegisterForm(request.POST or None)
    login_form    = UserLoginForm(request.POST or None)
    context['register_form'] = register_form
    context['login_form']    = login_form
    if register_form.is_valid():
        username  = register_form.cleaned_data.get('username', '')
        email     = register_form.cleaned_data.get('email', '')
        email2    = register_form.cleaned_data.get('email2', '')
        password1 = register_form.cleaned_data.get('password', '')
        password2 = register_form.cleaned_data.get('password2', '')
        first_name= register_form.cleaned_data.get('first_name', '')
        last_name = register_form.cleaned_data.get('last_name', '')
        phone     = register_form.cleaned_data.get('phone', '')

        if email and email2 and email != email2:
            return render(request, 'auth.html', {'error':"Emails must match"})
        if password1 and password2 and password1 != password2:
            return render(request, 'auth.html', {'error':"Passwords must match"})
        email_qs    = User.objects.filter(email=email)
        username_qs = User.objects.filter(username=username)
        if email_qs.exists() and username_qs.exists():
            register_message = "This email and username has already been registered"
            context['register_message'] = register_message
            return render(request, 'auth.html', context)
        if email_qs.exists():
            register_message = "This email has already been registered"
            context['register_message'] = register_message
            return render(request, 'auth.html', context)
        if username_qs.exists():
            register_message = "This username has already been registered"
            context['register_message'] = register_message
            return render(request, 'auth.html', context)

        user = User.objects.create_user(
            username=username, 
            email=email, 
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password1)
        user.is_active = False
        user.save()
        new_user = authenticate(username=user.username, password=password1)
        login(request, user)
        return redirect('home')
    return render(request, "auth.html", context)




def logout_view(request):
    logout(request)
    return redirect('login_view')
