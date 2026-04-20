def predict_performance(student_result, attendance_percentage):
    percentage = student_result.percentage

    if percentage >= 75 and attendance_percentage >= 80:
        prediction = "Excellent"
    elif percentage >= 60 and attendance_percentage >= 70:
        prediction = "Good"
    elif percentage >= 40:
        prediction = "Average"
    else:
        prediction = "At Risk"

    weak_subjects = []

    if student_result.math_marks < 50:
        weak_subjects.append("Math")
    if student_result.science_marks < 50:
        weak_subjects.append("Science")
    if student_result.english_marks < 50:
        weak_subjects.append("English")

    suggestions = []

    if "Math" in weak_subjects:
        suggestions.append("Revise Algebra, Basic Arithmetic, and Practice Daily Numericals")
    if "Science" in weak_subjects:
        suggestions.append("Focus on Concept Understanding, Diagrams, and Chapter-wise Revision")
    if "English" in weak_subjects:
        suggestions.append("Improve Grammar, Reading Comprehension, and Writing Practice")

    recommended_courses = []

    if prediction == "Excellent":
        recommended_courses = [
            "Advanced Aptitude Course",
            "Programming Fundamentals",
            "Logical Reasoning"
        ]
    elif prediction == "Good":
        recommended_courses = [
            "Intermediate Problem Solving",
            "Communication Skills",
            "Subject Revision Course"
        ]
    elif prediction == "Average":
        recommended_courses = [
            "Foundation Course in Weak Subjects",
            "Basic Time Management",
            "Exam Preparation Strategies"
        ]
    else:
        recommended_courses = [
            "Beginner Level Recovery Course",
            "Basic Subject Strengthening",
            "Daily Practice Plan"
        ]

    return {
        "prediction": prediction,
        "weak_subjects": weak_subjects,
        "suggestions": suggestions,
        "recommended_courses": recommended_courses
    }