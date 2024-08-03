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
            "hcc_student_portal.png",
            "hcc_student_portal2.png",
            "hcc_student_portal3.png",
            "hcc_student_portal4.png"
        ],
        "github": "https://github.com/sanquilouie/hccstudentportal"
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
            "barangay_information_system.png",
            "barangay_information_system2.png",
            "barangay_information_system3.png",
            "barangay_information_system4.png"
        ],
        "github": "https://github.com/sanquilouie/barangaytrackingsystem"
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
            "automated_coin_locker.jpg",
            "automated_coin_locker1.jpg",
            "automated_coin_locker1.jpg"
        ],
    }
    return render_template('project_details.html', project=project)

@app.route('/projects/tap-the-talaba')
def tap_the_talaba():
    project = {
        "title": "Tap the Talaba",
        "description": "A mobile game developed during college that combines elements from 2Fuse and Focus games. It features engaging gameplay with various levels and challenges.",
        "features": [
            "Color-matching gameplay",
            "Level progression with increasing difficulty",
            "Unique fusion of Fuse and Focus elements"
        ],
        "technologies": [
            "Java",
            "Android SDK"
        ],
        "images": [
            "Tap_the_Talaba.jpg",
            "Tap_the_Talaba2.jpg",
            "Tap_the_Talaba3.jpg",
            "Tap_the_Talaba4.jpg",
            "Tap_the_Talaba5.jpg",
        ],
        "github": "https://github.com/sanquilouie/tapthetalaba"
    }
    return render_template('project_details.html', project=project)

@app.route('/projects/pageant-tabulation-system')
def pageant_tabulation_system():
    project = {
        "title": "Pageant Tabulation System",
        "description": "The Pageant Tabulation System is a web application designed to streamline the tabulation of pageant results. Developed as a requirement project, it allows judges to vote for each candidate through individual panels. The system updates the current standings in real-time, allowing the tabulator to view and print the results efficiently.",
        "features": [
            "Real-time voting by judges",
            "Instant updates of candidate standings",
            "Printable results for official documentation",
            "User-friendly interface for both judges and tabulator"
        ],
        "technologies": [
            "PHP",
            "HTML",
            "CSS"
        ],
        "images": [
            "Pageant_Tabulation.png",
            "Pageant_Tabulation2.png",
            "Pageant_Tabulation3.png",
        ],
        "github": "https://github.com/sanquilouie/pageant_tabulation_system"
    }
    return render_template('project_details.html', project=project)


