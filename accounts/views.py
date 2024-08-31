from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            form.save()
            messages.success(request, "Your account has been Registered Successfully...!")

            return redirect('registerUser')
        else:
            messages.error(request, "Invalid Form...!")

            return redirect('registerUser')

    else:
        form = UserForm()
        context = {
            'form': form,
        }
    return render(request, 'accounts/registerUser.html', context)
   