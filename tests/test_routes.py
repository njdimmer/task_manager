"""Tests for the task manager routes."""

from app.models import Task, db


def test_add_task(client, app):
    """Test adding a new task."""
    response = client.post('/add_task', data={'title': 'Added Task'}, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        task = db.session.execute(db.select(Task).filter_by(title='Added Task')).scalar_one()
        assert task is not None
        assert task.title == 'Added Task'
        assert not task.completed


def test_complete_task(client, app):
    """Test completing a task."""
    with app.app_context():
        task = Task(title='Test Task')
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.get(f'/complete_task/{task_id}', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        updated_task = db.session.execute(db.select(Task).filter_by(id=task_id)).scalar_one()
        assert updated_task.completed


def test_delete_task(client, app):
    """Test deleting a task."""
    with app.app_context():
        task = Task(title='Test Task')
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.get(f'/delete_task/{task_id}', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        deleted_task = db.session.execute(db.select(Task).filter_by(id=task_id)).scalar_one_or_none()
        assert deleted_task is None


def test_invalid_task_routes(client):
    """Test accessing invalid task IDs."""
    invalid_id = 999
    assert client.get(f'/complete_task/{invalid_id}').status_code == 404
    assert client.get(f'/delete_task/{invalid_id}').status_code == 404


def test_empty_task_title(client):
    """Test adding task with empty title."""
    response = client.post('/add_task', data={'title': ''}, follow_redirects=True)
    assert response.status_code == 400
