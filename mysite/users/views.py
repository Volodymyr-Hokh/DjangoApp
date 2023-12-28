from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            login(request, new_user)
            return redirect("records:index")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "registration/register.html", context)
