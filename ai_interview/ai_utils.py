from groq import Groq
from django.conf import settings
import json
import re


def generate_questions_from_resume(resume_text: str) -> str:
    """
    Generate exactly 10 resume-based + 2 general English proficiency questions.
    Returns a numbered list as a plain string (for storage in session.questions).
    """
    try:
        client = Groq(api_key=settings.GROQ_API_KEY)

        prompt = f"""
You are NEXUS, a professional AI interviewer conducting a technical + HR interview.

Study the following resume carefully:

--- RESUME START ---
{resume_text}
--- RESUME END ---

Your task: Generate EXACTLY 12 interview questions in the following format:

- Questions 1 to 10: Technical/professional questions directly based on the skills,
  projects, experience, tools, and technologies mentioned in this specific resume.
  Each question must be unique and tailored to THIS candidate's background.

- Questions 11 and 12: General English speaking proficiency questions.
  These should test fluency, confidence, and communication skills.
  Example topics: self-introduction, strengths/weaknesses, career goals.

OUTPUT FORMAT (strict):
Return ONLY a numbered list, nothing else. No preamble, no explanation.
Each line must follow this exact pattern:

1. [Question text here]
2. [Question text here]
...
12. [Question text here]

Ensure questions are clear, concise, and suitable for a spoken verbal interview.
Do NOT use markdown, asterisks, bold, or any special formatting inside questions.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500,
        )

        raw = response.choices[0].message.content.strip()
        return _clean_questions(raw)

    except Exception as e:
        # Return safe fallback questions so the interview can still run
        return _fallback_questions(str(e))


def _clean_questions(raw: str) -> str:
    """
    Normalize the raw LLM output into a clean numbered list.
    Strips markdown artifacts like **, __, ## etc.
    """
    lines = raw.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Remove markdown bold/italic/heading markers
        line = re.sub(r'\*{1,3}', '', line)
        line = re.sub(r'_{1,3}', '', line)
        line = re.sub(r'^#{1,6}\s*', '', line)
        # Keep only lines that start with a number
        if re.match(r'^\d+[\.\)]\s+.{10,}', line):
            cleaned.append(line)

    # If parsing failed, return the raw text as-is (safe fallback)
    if len(cleaned) < 6:
        return raw

    return '\n'.join(cleaned[:12])


def _fallback_questions(error_note: str) -> str:
    """
    Safe fallback if Groq API fails. Returns generic questions.
    """
    return """1. Can you walk me through your professional background and key skills?
2. What programming languages or technologies are you most comfortable with?
3. Describe a challenging project you worked on and how you handled it.
4. How do you approach problem-solving when you encounter a technical blocker?
5. What tools do you use for version control and collaboration?
6. Have you worked in an Agile or Scrum environment? Describe your experience.
7. How do you ensure code quality in your projects?
8. Describe your experience with databases — both SQL and NoSQL if applicable.
9. What is your experience with APIs — designing, consuming, or documenting them?
10. Where do you see yourself technically in the next 2 to 3 years?
11. Please introduce yourself in a few sentences — your name, background, and what excites you professionally.
12. What do you consider your greatest strength, and can you give an example of it in action?"""


def parse_questions_to_list(questions_text: str) -> list[str]:
    """
    Utility: Convert the stored questions string into a Python list.
    Useful for views or API endpoints.
    """
    lines = questions_text.strip().split('\n')
    result = []
    for line in lines:
        line = line.strip()
        m = re.match(r'^\d+[\.\)]\s*(.+)', line)
        if m:
            result.append(m.group(1).strip())
        elif len(line) > 20 and not line.startswith('#'):
            result.append(line)
    return result[:12]