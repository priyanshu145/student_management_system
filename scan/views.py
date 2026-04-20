import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# try import (safe)
try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False


# ---------------- TEXT ANALYSIS ----------------

def analyze_exam_text(extracted_text):
    text = extracted_text.strip()

    if not text:
        return {
            "score": 0,
            "status": "No readable text found",
            "word_count": 0,
            "line_count": 0,
            "keywords_found": [],
            "remarks": "Image uploaded but text not detected properly."
        }

    words = text.split()
    word_count = len(words)

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    line_count = len(lines)

    keywords = [
        "definition", "example", "advantages", "disadvantages",
        "python", "django", "database", "algorithm",
        "function", "method", "class", "inheritance",
        "sql", "html", "css", "javascript", "framework"
    ]

    found_keywords = []
    lower_text = text.lower()

    for word in keywords:
        if word in lower_text:
            found_keywords.append(word)

    # scoring
    score = 0

    if word_count >= 30:
        score += 20
    if word_count >= 80:
        score += 20
    if line_count >= 3:
        score += 15
    if line_count >= 6:
        score += 15
    if len(found_keywords) >= 2:
        score += 15
    if len(found_keywords) >= 5:
        score += 15

    score = min(score, 100)

    if score >= 75:
        status = "Good Answer"
        remarks = "Detailed and meaningful answer."
    elif score >= 45:
        status = "Average Answer"
        remarks = "Answer is okay but can be improved."
    else:
        status = "Weak Answer"
        remarks = "Answer is too short or unclear."

    return {
        "score": score,
        "status": status,
        "word_count": word_count,
        "line_count": line_count,
        "keywords_found": found_keywords,
        "remarks": remarks
    }


# ---------------- SCAN VIEW ----------------

def scan_upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        if not image:
            return render(request, 'scan/scan_upload.html', {
                'error': 'Please select an image first.'
            })

        # save image
        scan_dir = os.path.join(settings.MEDIA_ROOT, 'scans')
        os.makedirs(scan_dir, exist_ok=True)

        fs = FileSystemStorage(location=scan_dir)
        filename = fs.save(image.name, image)
        file_url = fs.url(filename)
        file_path = os.path.join(scan_dir, filename)

        # check easyocr availability
        if not EASYOCR_AVAILABLE:
            return render(request, 'scan/result.html', {
                'message': 'OCR library not installed',
                'error': 'Please install easyocr using: pip install easyocr'
            })

        try:
            reader = easyocr.Reader(['en'], gpu=False)
            results = reader.readtext(file_path, detail=0)

            extracted_text = "\n".join(results)

            analysis = analyze_exam_text(extracted_text)

            return render(request, 'scan/result.html', {
                'message': 'Image uploaded and analyzed successfully!',
                'image_url': file_url,
                'extracted_text': extracted_text,
                'analysis': analysis
            })

        except Exception as e:
            return render(request, 'scan/result.html', {
                'message': 'Image uploaded but analysis failed.',
                'error': str(e)
            })

    return render(request, 'scan/scan_upload.html')