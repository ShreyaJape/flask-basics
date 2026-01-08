"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Shreya Jape',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'your.shreyaj4@gmail.com',
    'github': 'https://github.com/ShreyaJape',
    'linkedin': 'https://linkedin.com/in/Shreya-jape',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
]

PROJECTS = [
    {
        'id': 1,
        'name': 'Personal Website',
        'description': 'A Flask-powered personal portfolio website.',
        'tech': ['Python', 'Flask', 'HTML', 'CSS'],
        'status': 'Completed'
    },
    {
        'id': 2,
        'name': 'Online Exam Management System',
        'description': 'A web-based system that allows admins and students to manage exams.',
        'tech': ['Python', 'Flask', 'SQLite', 'HTML', 'CSS'],
        'status': 'In Progress',
        'features': [
            'Admin login',
            'Student login',
            'Exam creation',
            'Automatic result evaluation'
        ],
        'modules': [
            'Admin Module',
            'Student Module',
            'Exam Module',
            'Result Module'
        ],
        'role': 'Backend Developer',
        'learning': 'Flask routing, templates, database integration'
    },
    {
        'id': 3,
        'name': 'Trustfix – Home Service Website',
        'description': 'A service booking platform.',
        'tech': ['Flask', 'HTML', 'CSS'],
        'status': 'Planned'
    }
]


BLOG_POSTS = [
    {
        'id': 1,
        'title': 'My Journey with Flask',
        'summary': 'How I started learning Flask and built my first web app.',
        'content': 'Flask is a lightweight Python framework that helped me understand backend development.',
        'date': '10 Jan 2026'
    },
    {
    'id': 2,
    'name': 'Online Exam Management System',
    'description': 'A web-based system that allows administrators to create exams, manage students, and conduct online tests securely.',
    'tech': ['Python', 'Flask', 'SQLite', 'HTML', 'CSS'],
    'status': 'In Progress',

    # 🔽 ADD THESE EXTRA DETAILS
    'features': [
        'Admin login and authentication',
        'Student registration and login',
        'Online exam creation',
        'Automatic result evaluation',
        'Secure question handling'
    ],
    'modules': [
        'Admin Module',
        'Student Module',
        'Exam Module',
        'Result Module'
    ],
    'role': 'Backend Developer',
    'learning': 'Learned Flask routing, template rendering, and database integration'
},

    {
        'id': 3,
        'title': 'Future Goals',
        'summary': 'My goals as a computer engineering student.',
        'content': 'I want to become a full-stack developer and work on real-world projects.',
        'date': '20 Jan 2026'
    }
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        info=PERSONAL_INFO,
        blogs=BLOG_POSTS
    )

@app.route('/exam-ui')
def exam_ui():
    return render_template('exam_ui.html', info=PERSONAL_INFO)



if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
