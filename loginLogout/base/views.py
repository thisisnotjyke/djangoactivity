from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# login
@login_required
def profile(request):
 return render(request, "profile.html", {})

# logout
def logoutaccount(request):
 logout(request)
 return redirect('/accounts/login/')

# Create your views here.
def profile(request):
 user = request.user
 context = {'profile': profile}
 return render(request, 'profile.html', context)