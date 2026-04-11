from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from teacher.models import Teacher
from student.models import Student
from result.models import Result

@login_required
def add_marks(request):
    if not Teacher.objects.filter(user=request.user).exists():
        return render(request, 'teacher/add_marks.html', {
            'error': 'Access denied. Only teachers can add marks.'
        })

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject1 = request.POST.get('subject1')
        marks1 = request.POST.get('marks1')
        subject2 = request.POST.get('subject2')
        marks2 = request.POST.get('marks2')
        subject3 = request.POST.get('subject3')
        marks3 = request.POST.get('marks3')
        subject4 = request.POST.get('subject4')
        marks4 = request.POST.get('marks4')
        subject5 = request.POST.get('subject5')
        marks5 = request.POST.get('marks5')

        try:
            student = Student.objects.get(id=student_id)

            if Result.objects.filter(student=student).exists():
                students = Student.objects.all()
                return render(request, 'teacher/add_marks.html', {
                    'students': students,
                    'error': 'Result already exists for this student.'
                })

            Result.objects.create(
                student=student,
                subject1=subject1,
                marks1=marks1,
                subject2=subject2,
                marks2=marks2,
                subject3=subject3,
                marks3=marks3,
                subject4=subject4,
                marks4=marks4,
                subject5=subject5,
                marks5=marks5,
            )

            students = Student.objects.all()
            return render(request, 'teacher/add_marks.html', {
                'students': students,
                'success': 'Marks added successfully.'
            })

        except Student.DoesNotExist:
            students = Student.objects.all()
            return render(request, 'teacher/add_marks.html', {
                'students': students,
                'error': 'Student not found.'
            })

    students = Student.objects.all()
    return render(request, 'teacher/add_marks.html', {
        'students': students
    })