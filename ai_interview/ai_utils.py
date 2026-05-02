import google.generativeai as genai
from django.conf import settings


def generate_questions_from_resume(resume_text):
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)

        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        You are an AI interviewer.

        Read this resume and generate 10 professional interview questions related to skills and to check english speaking proficiency.

        Resume:
        {resume_text}
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"