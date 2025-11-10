from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import SignupForm, ProfileForm, UserForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro completado.")
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, instance=request.user)
        pf = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uf.is_valid() and pf.is_valid():
            uf.save()
            pf.save()
            messages.success(request, "Perfil actualizado.")
            return redirect('accounts:profile')
    else:
        uf = UserForm(instance=request.user)
        pf = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile_form.html', {'uf': uf, 'pf': pf})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:profile')
