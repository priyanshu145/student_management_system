from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from student.models import Student
from teacher.models import Teacher
from result.models import Result

# Create your views here.

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        
        user =authenticate(username=username, password=password)
        
        #check if user is not none
        if user is not None:
            
            #if user is student
            if Student.objects.filter(user=user).exists():
               login(request, user)
               return redirect('authentication:student_dashboard')
            else :
                return render(request, 'authentication/student_login.html' , 
                              {'Error': 'you are not a student'})
        
        else :
            return render(request, 'authentication/student_login.html', {'Error': 'invalid user name or password'})        
    
        
            
    return render(request, 'authentication/student_login.html')

@login_required
def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username= username, password= password)
        #check if user is not none
        if user is not None:
            #check if user is teacher
            if Teacher.objects.filter(user=user).exists():
                login (request, user)
                return redirect('authentication:teacher_dashboard')
            else:
                return render(request, 'authentication/teacher_login.html', {'Error': "teacher doesn't exist"})
        
        
        else:
            return render(request, 'teacher_login.html', {'ERROR':'invalid user name or password '})
    return render(request, 'authentication/teacher_login.html' , {'Error': 'you are not a teacher'})

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher/teacher_dashboard.html')
    
    


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




def result_login(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        date_of_birth = request.POST.get('date_of_birth')

        try:
            student = Student.objects.get(
                roll_no=roll_no,
                date_of_birth=date_of_birth
            )

            result = Result.objects.get(student=student)

            return render(request, 'result/result_dash.html', {
                'student': student,
                'result': result
            })

        except Student.DoesNotExist:
            return render(request, 'authentication/result_login.html', {
                'error': 'Invalid roll number or date of birth'
            })

        except Result.DoesNotExist:
            return render(request, 'authentication/result_login.html', {
                'error': 'Result not found'
            })

    return render(request, 'authentication/result_login.html')