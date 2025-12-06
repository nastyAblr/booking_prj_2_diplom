from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from authapp.forms import (
    TravelUserRegisterForm,
    TravelUserLoginForm,
    TravelUserEditForm,
    TravelUserProfileEditForm,
   )

# Регистрация пользователя
def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = TravelUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = TravelUserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


# Логин
def login_view(request):
    title = 'вход'


    login_form = TravelUserLoginForm(request=request, data=request.POST or None)

    next_page = request.GET.get('next', '')

    if request.method == 'POST' and login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        # user = auth.authenticate(username=username, password=password)
        user = auth.authenticate(request=request, username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(request.POST.get('next') or reverse('mainapp:main'))
        else:
            # опционально: добавить сообщение об ошибке
            login_form.add_error(None, "Неверное имя пользователя или пароль")

    content = {
        'title': title,
        'login_form': login_form,
        'next': next_page
    }

    return render(request, 'authapp/login.html', content)


# ЛОГАУТ
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))


# Редактирование ПРОФИЛЯ и АККАУНТА
@login_required
def edit(request):
    title = 'редактирование профиля'

    if request.method == 'POST':
        user_form = TravelUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = TravelUserProfileEditForm(request.POST, instance=request.user.traveluserprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        user_form = TravelUserEditForm(instance=request.user)
        profile_form = TravelUserProfileEditForm(instance=request.user.traveluserprofile)

    content = {
        'title': title,
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/edit.html', content)
