# Task Manager App
A simple Flask-based web application for managing tasks with CRUD operations. The app uses SQLAlchemy for interacting with a PostgreSQL database to store tasks and their statuses.

# Overview
Task Manager is a lightweight web application that helps you manage tasks with the following features:

* Create tasks: Add tasks with titles.
* Read tasks: View a list of tasks.
* Update tasks: Mark tasks as complete or incomplete.
* Delete tasks: Remove tasks from the list.

The app uses Flask as the web framework and SQLAlchemy for the database layer. The database is backed by PostgreSQL.

## Usage

### Running Locally

To run the app locally with a temporary SQLite database, follow these steps:

1. Install the required dependencies:
    ``` bash    
    pip install -r requirements.txt
    ```

2. Run the app using the following command:
    
    ``` bash
    python -m task_manager.app.run
    ```

This command will start the Flask development server, and an in-memory SQLite database will be created automatically for the app. The server will be available at http://127.0.0.1:5000.