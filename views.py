from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects/hcc-student-portal')
def hcc_student_portal():
    project = {
        "title": "HCC Student Portal",
        "description": "A comprehensive student management system developed using PHP and SQL. It features user authentication, grade tracking, and course management.",
        "features": [
            "User authentication",
            "Grade tracking",
            "Course management",
            "Responsive design"
        ],
        "technologies": [
            "PHP",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "images": [
            "hcc_student_portal1.png",
            "hcc_student_portal2.png",
            "hcc_student_portal3.png"
        ],
        "github": "https://github.com/yourusername/hcc-student-portal"
    }
    return render_template('project_details.html', project=project)

@app.route('/projects/barangay-information-tracking-system')
def barangay_information_tracking_system():
    project = {
        "title": "Barangay Information Tracking System",
        "description": "A system for tracking barangay information, including resident details and services, built with PHP and SQL. It streamlines data management and retrieval.",
        "features": [
            "Resident details management",
            "Service tracking",
            "Data management",
            "User-friendly interface"
        ],
        "technologies": [
            "PHP",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "images": [
            "barangay_information_tracking_system1.png",
            "barangay_information_tracking_system2.png"
        ],
        "github": "https://github.com/yourusername/barangay-information-tracking-system"
    }
    return render_template('project_details.html', project=project)


@app.route('/projects/automated-coin-locker')
def automated_coin_locker():
    project = {
        "title": "Automated Coin Locker",
        "description": "An innovative locker system that uses Java for the GUI and functionalities, Raspberry Pi for the touchscreen panel, and Arduino for controlling the lockers.",
        "features": [
            "Java GUI and functionalities",
            "Raspberry Pi touchscreen panel",
            "Arduino for locker control",
            "Automated and user-friendly design"
        ],
        "technologies": [
            "Java",
            "Raspberry Pi",
            "Arduino"
        ],
        "images": [
            "automated_coin_locker1.png",
            "automated_coin_locker2.png"
        ],
        "github": "https://github.com/yourusername/automated-coin-locker"
    }
    return render_template('project_details.html', project=project)

