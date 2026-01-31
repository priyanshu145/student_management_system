from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    
    return render(request, 'main_app/index.html')

@login_required
def logout_views(request):
    if request.method == 'POST':
       logout(request)
       return redirect('main_app:index')
    
    return redirect('main_app:index')
    
