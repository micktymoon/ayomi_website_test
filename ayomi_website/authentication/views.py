from django.shortcuts import render, redirect
from django.contrib.auth import login
from ayomi_website.authentication.forms import SignUpForm, ChangeEmailForm


def signup(request):
    """A view that displays the new account registration form.
    And save the new account to the database."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
        else:
            form = SignUpForm()
            return render(request, 'authentication/signup.html',
                          {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'authentication/signup.html', {'form': form})


def account_view(request):
    """A view that displays the details of a user account."""
    user = request.user
    form = ChangeEmailForm()
    return render(request, 'authentication/account.html',
                  {'user': user, 'form': form})


def change_email(request):
    form = ChangeEmailForm(request.POST)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            if form.is_valid():
                user.email = form.cleaned_data['email']
                user.save()
                return render(request, 'authentication/account.html',
                              {'user': user, 'form': form})
            else:
                redirect('account')
        else:
            return redirect('login')
    else:
        redirect('account')
