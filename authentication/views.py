from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from student.models import Student
from teacher.models import Teacher
from result.models import Result


# ---------------- STUDENT ----------------

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if Student.objects.filter(user=user).exists():
                login(request, user)
                return redirect('authentication:student_dashboard')
            else:
                return render(request, 'authentication/student_login.html', {
                    'error': 'You are not a student'
                })
        else:
            return render(request, 'authentication/student_login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'authentication/student_login.html')


@login_required
def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')


# ---------------- TEACHER ----------------

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if Teacher.objects.filter(user=user).exists():
                login(request, user)
                return redirect('authentication:teacher_dashboard')
            else:
                return render(request, 'authentication/teacher_login.html', {
                    'error': "Teacher doesn't exist"
                })
        else:
            return render(request, 'authentication/teacher_login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'authentication/teacher_login.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'teacher/teacher_dashboard.html')


# ---------------- ADMIN ----------------

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
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
    return render(request, 'admin_panel/admin_dashboard.html')  # fixed name


# ---------------- RESULT ----------------

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


# ---------------- AI ----------------

def ai_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if Student.objects.filter(user=user).exists():
                login(request, user)
                return redirect('authentication:ai_analysis')
            else:
                return render(request, 'authentication/ai_login.html', {
                    'error': 'You are not a student'
                })
        else:
            return render(request, 'authentication/ai_login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'authentication/ai_login.html')


@login_required
def ai_analysis(request):
    return render(request, 'student/ai_analysis.html')