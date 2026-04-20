🎓 Student Management System

A full-featured Student Management System built with Django that helps manage students, teachers, attendance, results, and assignments in an organized and efficient way.

📌 Table of Contents
About Project
Features
Tech Stack
System Architecture
Project Structure
Installation & Setup
Usage
Screenshots
Future Improvements
Contributing
License
Author

📖 About Project

The Student Management System is a web-based application designed to simplify the management of student-related data in educational institutions.

It provides separate dashboards for Admin, Teachers, and Students, making it easier to handle:

Student records
Attendance tracking
Academic results
Assignment management

🚀 Features
👨‍💼 Admin Panel
Add / Manage Students
Add / Manage Teachers
Assign subjects
View reports & analytics

👩‍🏫 Teacher Panel
Take attendance
Upload results
Manage subjects
Upload assignments

👨‍🎓 Student Panel
View attendance
Check results
Access assignments
View class details

🔐 Authentication System
Secure login/logout
Role-based access control

🛠️ Tech Stack
Category	Technology
Backend = Python, Django
Frontend = HTML, CSS
Database =	MySQL

⚙️ Installation & Setup
🔽 1. Clone the Repository
git clone https://github.com/harry7705/student_management_system.git
cd student_management_system

🐍 2. Create Virtual Environment
python -m venv venv

▶️ 3. Activate Virtual Environment
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Mac/Linux

📦 4. Install Dependencies
pip install django

🗄️ 5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

👤 6. Create Superuser
python manage.py createsuperuser

▶️ 7. Run Server
python manage.py runserver

🌐 Usage
Open browser → http://127.0.0.1:8000/
Login using credentials
Navigate based on role:
Admin
Teacher
Student

📸 Screenshots
(Soon)

🤝 Contributing
Contributions are always welcome!

# Steps
1. Fork the repository
2. Create new branch (git checkout -b feature-name)
3. Commit changes (git commit -m "Add feature")
4. Push branch (git push origin feature-name)
5. Open Pull Request

📜 License
This project is licensed under the MIT License.

👤 Author
Harry
Priyanshu

GitHub: https://github.com/harry7705
GitHub: https://github.com/priyanshu145
