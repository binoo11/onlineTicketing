from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterCustomerForm

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            messages.info(request, 'Your account has been sucessfully registered. Please login to continue')
            return redirect('login')
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field}: {error}")
           # messages.error(request,'Something went wrong. Please check form inputs')
            return redirect('register_customer')
    else: form = RegisterCustomerForm()
    context = {'form': form}
    return render(request,'users/register_customer.html', context)

#login a user

def lofin_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request,'Login sucessfull.Please enjoy session')
            return redirect('dashboard')
        else:

            messages.warning(request,'Something went wrong. Please check form inputs')
            return redirect('login')
    else:
        return render(request,'users/login.html')
    
    #logout a use

def logout_user(request):
    logout(request)
    messages.info(request,'Your session has end.Please log in to continue')
    return redirect('login')
    

