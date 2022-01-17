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
    if request.user.is_authenticated:
        user = request.user
        form = ChangeEmailForm()
        return render(request, 'authentication/account.html',
                      {'user': user, 'form': form})
    else:
        return redirect('login')


def change_email(request):
    """A view that changes the user's password"""
    form = ChangeEmailForm(request.POST)
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            if form.is_valid():
                user.email = form.cleaned_data['email']
                user.save()
                return render(request, 'authentication/account.html',
                              {'user': user, 'form': form})
            else:
                render(request, 'authentication/account.html',
                       {'user': user, 'form': form})
        else:
            render(request, 'authentication/account.html',
                   {'user': user, 'form': form})
    else:
        return redirect('login')
