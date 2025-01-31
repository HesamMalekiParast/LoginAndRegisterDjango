from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from .forms import SignUpForm, LoginForm


class RegisterView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, 'Registration successful! Welcome.')  # Success message
            return redirect('home')  # Redirect to home or another page after successful registration
        else:
            messages.error(request, 'There was an error in the form. Please try again.')  # Error message
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user using email
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('home')  # Redirect to home or another page after login
            else:
                form.add_error('email', 'Invalid email or password')
                messages.error(request, 'Invalid email or password. Please try again.')  # Error message
        return render(request, 'login.html', {'form': form})
