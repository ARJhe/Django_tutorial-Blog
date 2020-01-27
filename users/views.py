from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        messages.error(request, f'Not open registration yet!')
        return redirect('register')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # we should save it
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# decorator prevent the state which not login direct to here
@login_required
def profile(request):
    return render(request, 'users/profile.html')