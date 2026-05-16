from django.shortcuts import render, redirect, get_object_or_404
from .models import InterviewSession
from .utils import extract_resume_text          # updated function name (also keeps extract_pdf_text alias)
from .ai_utils import generate_questions_from_resume


def upload_resume(request):
    if request.method == "POST":
        resume = request.FILES.get("resume")
        if not resume:
            return render(request, 'ai_interview/upload_resume.html', {'error': 'Please select a resume file.'})

        session = InterviewSession.objects.create(
            user=request.user if request.user.is_authenticated else None,
            resume=resume,
        )

        # Extract text — handles PDF, DOCX, TXT
        resume_text = extract_resume_text(session.resume.path)

        # Generate tailored questions (10 resume-based + 2 general)
        questions = generate_questions_from_resume(resume_text)

        session.resume_text = resume_text
        session.questions   = questions
        session.save()

        return redirect('ai_interview:video_interview', session_id=session.id)

    return render(request, 'ai_interview/upload_resume.html')


def video_interview(request, session_id):
    session = get_object_or_404(InterviewSession, id=session_id)
    return render(request, 'ai_interview/interview_session.html', {
        'session': session,
    })