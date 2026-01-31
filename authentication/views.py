from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from student.models import Student

# Create your views here.

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user =authenticate(username=username, password=password)
        
        #check if user is not none
        if user is not None:
            
            #if user is student
            if Student.objects.filter(user=user).exists():
               login (request, user)
               return redirect('authentication:student_dashboard')
            else :
                return render(request, 'authentication/student_login.html' , 
                              {'Error': 'you are not a student'})
        
        else :
            return render(request, 'authenticatetion/student_login.html', {'Error': 'invalid user name or password'})        
    
        
            
    return render(request, 'authentication/student_login.html' , {'Error': 'you are not a student'})

@login_required
def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')



def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # CHECK 1: user exists
        if user is not None:
            # CHECK 2: user is admin (superuser)
            if user.is_superuser:
                login(request, user)
                return redirect('authentication:admin_dashboard')
            else:
                return render(request, 'authentication/admin_login.html', {
                    'error': 'You are not an admin'
                })
        else:
            return render(request, 'authentication/admin_login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'authentication/admin_login.html')


@login_required
def admin_dashboard(request):
    return render(request, 'admin_panal/admin_dashboard.html')    
