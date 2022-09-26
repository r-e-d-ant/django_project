from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# The views here.
def register(request):
    # instance of the form
    form = UserCreationForm()
    return render(request, 'users/register.html', { 'form' : form })