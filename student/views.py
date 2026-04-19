from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Student
from result.models import Result
from .ai_utils import predict_performance


@login_required
def ai_analysis(request):
    student = Student.objects.filter(user=request.user).first()

    if not student:
        return render(request, 'student/ai_analysis.html', {
            'error': 'Student profile not found'
        })

    result = Result.objects.filter(student=student).first()

    if not result:
        return render(request, 'student/ai_analysis.html', {
            'error': 'Result data not found',
            'student': student,
        })

    attendance_percentage = 72

    analysis = predict_performance(result, attendance_percentage)

    context = {
        'student': student,
        'result': result,
        'attendance_percentage': attendance_percentage,
        'prediction': analysis.get('prediction', 'Not Available'),
        'weak_subjects': analysis.get('weak_subjects', []),
        'suggestions': analysis.get('suggestions', []),
        'recommended_courses': analysis.get('recommended_courses', []),
    }

    return render(request, 'student/ai_analysis.html', context)