from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ======================================================
# In-memory data (No database – resets on server restart)
# ======================================================
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# ======================================================
# ROUTES
# ======================================================

# Home Page – Dashboard
@app.route('/')
def home():
    return render_template('index.html', tasks=TASKS)


# Add Task Page (GET + POST)
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        priority = request.form['priority']

        new_task = {
            'id': TASKS[-1]['id'] + 1 if TASKS else 1,
            'title': title,
            'status': 'Pending',
            'priority': priority
        }

        TASKS.append(new_task)
        return redirect(url_for('home'))

    return render_template('add.html')


# View Single Task
@app.route('/task/<int:id>')
def task_detail(id):
    task = None
    for t in TASKS:
        if t['id'] == id:
            task = t
            break

    return render_template('task.html', task=task)


# Mark Task as Completed
@app.route('/complete/<int:id>')
def complete_task(id):
    for task in TASKS:
        if task['id'] == id:
            task['status'] = 'Completed'
            break

    return redirect(url_for('home'))


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# ======================================================
# RUN APP
# ======================================================
if __name__ == '__main__':
    app.run(debug=True)
