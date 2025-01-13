from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import redirect, render
from .forms import UserAccountCreationForm, UserAccountUpdateForm, UserProfileUpdateForm
from tools import context


def register(request):
    context['form_name'] = 'Register'
    context['form'] = UserAccountCreationForm()
    context['button_text'] = 'Register'

    if request.method == 'POST':
        form = UserAccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user-login')

    return render(request, 'form_page.html', context)

def login(request):
    context['form_name'] = 'Login'
    context['form'] = AuthenticationForm()
    context['button_text'] = 'Login'

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.error_messages)
        print(form.data)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth.login(request, user)
                return redirect('user-account', username=user.username)
            else:
                context['message'] = 'Login failed.'
        else:
            context['errors'] = form.error_messages
 
    return render(request, 'form_page.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('user-login')

@login_required
def user_account(request, username):
    profile = request.user.get_user_profile()
    context['profile'] = profile
    return render(request, 'user_account.html', context)

@login_required
def user_update(request, username):
    context['form_name'] = 'Update User Details'
    context['account_form'] = UserAccountUpdateForm(instance=request.user)
    context['profile_form'] = UserProfileUpdateForm(instance=request.user.get_user_profile())
    context['button_text'] = 'Update'
    
    if request.method == 'POST':
        account_form = UserAccountUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.get_user_profile())
        if account_form.is_valid() and profile_form.is_valid():
            account_form.save()
            profile_form.save()
            return redirect('user-account', username)

    return render(request, 'user_update.html', context)
