#!/usr/bin/env python3

"""App entry point."""

from . import db, create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
