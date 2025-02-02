"""Test Task model."""

from datetime import datetime
from app.models import Task, db


def test_task_model_creation(app):
    """Test Task model creation and default values."""
    with app.app_context():
        task = Task(title='Test Task')
        db.session.add(task)
        db.session.commit()

        assert task.title == 'Test Task'
        assert not task.completed
        assert isinstance(task.created_date, datetime)


def test_task_model_representation(app):
    """Test Task model string representation."""
    with app.app_context():
        task = Task(title='Test Task')
        assert str(task) == '<Task Test Task>'
