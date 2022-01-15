from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import get_user_model, login
from ayomi_website.authentication.forms import SignUpForm


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


class AccountView(DetailView):
    """A view that displays the details of a user account."""
    model = get_user_model()
    template_name = 'authentication/account.html'

    def get_object(self, queryset=None):
        return self.request.user
