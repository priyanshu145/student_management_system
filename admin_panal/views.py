from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from student.models import Student
from teacher.models import Teacher

@login_required
def add_student(request):

    # only admin allowed
    if not request.user.is_superuser:
        return render(request, 'error.html')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        roll_no = request.POST.get('roll_no')
        email = request.POST.get('email')
        course = request.POST.get('course')

        # check username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'admin_panal/add_student.html', {
                'error': 'Username already exists'
            })

        # create login user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        # create student profile
        Student.objects.create(
            user=user,
            full_name=full_name,
            roll_no=roll_no,
            email=email,
            course=course
        )

        return render(request, 'admin_panal/add_student.html', {
            'success': 'Student added successfully'
        })

    return render(request, 'admin_panal/add_student.html')


#adding teacher
@login_required
def add_teacher(request):

    if not request.user.is_superuser:
        return render(request, 'error.html', {'error': 'Access denied'})

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')

        # simple validation
        if not all([full_name, username, password, email]):
            return render(request, 'admin_panal/add_teacher.html', {
                'error': 'Please fill all required fields'
            })

        # check username
        if User.objects.filter(username=username).exists():
            return render(request, 'admin_panal/add_teacher.html', {
                'error': 'Username already exists'
            })

        # create user + teacher
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        Teacher.objects.create(
            user=user,   # must exist in model
            full_name=full_name,
            email=email,
            phone=phone,
            salary=salary,
            qualification=qualification,
            experience=experience
        )

        return render(request, 'admin_panal/add_teacher.html', {
            'success': 'Teacher added successfully'
        })

    return render(request, 'admin_panal/add_teacher.html')
    


# Create your views here.
@login_required
def view_students(request):
    students = Student.objects.all()
    return render(request, 'admin_panal/view_students.html', {'students': students})

@login_required
def edit_student(request, id):
     student = get_object_or_404(Student, id=id)
     
     if request.method == 'POST':
        student.full_name = request.POST['name']
        student.roll_no = request.POST['roll_no']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('admin_panal:view_students')

     return render(request, 'admin_panal/edit_student.html', {'student': student})
    

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student:view_students')

    return render(request, 'admin_panal/delete_student.html', {'student': student})