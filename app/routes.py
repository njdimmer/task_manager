from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Render the main page with all tasks."""
    tasks = db.session.execute(db.select(Task).order_by(Task.created_date.desc())).scalars().all()
    return render_template('index.html', tasks=tasks)


@main.route('/add_task', methods=['POST'])
def add_task():
    """Create a new task and add it to the database."""
    title = request.form['title']
    if not title or len(title) > 100:
        return '', 400
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/complete_task/<int:id>')
def complete_task(id):
    """Toggle completion status of a task."""
    task = db.session.get(Task, id)
    if not task:
        return '', 404
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/delete_task/<int:id>')
def delete_task(id):
    """Delete a task from the database."""
    task = db.session.get(Task, id)
    if not task:
        return '', 404
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
