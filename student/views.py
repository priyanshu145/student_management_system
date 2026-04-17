from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Student
from result.models import Result
from .ai_utils import predict_performance


@login_required
def ai_analysis(request):
    try:
        student = Student.objects.get(user=request.user)
        result = Result.objects.get(student=student)

        # for now static attendance
        attendance_percentage = 72

        analysis = predict_performance(result, attendance_percentage)

        context = {
            'student': student,
            'result': result,
            'attendance_percentage': attendance_percentage,
            'prediction': analysis['prediction'],
            'weak_subjects': analysis['weak_subjects'],
            'suggestions': analysis['suggestions'],
            'recommended_courses': analysis['recommended_courses'],
        }

        return render(request, 'student/ai_analysis.html', context)

    except Student.DoesNotExist:
        return render(request, 'student/ai_analysis.html', {
            'error': 'Student profile not found'
        })

    except Result.DoesNotExist:
        return render(request, 'student/ai_analysis.html', {
            'error': 'Result data not found'
        })

