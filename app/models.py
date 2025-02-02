"""Database models."""

from datetime import datetime
from . import db


class Task(db.Model):
    """Database model for representing tasks."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """String representation of task."""
        return f'<Task {self.title}>'
