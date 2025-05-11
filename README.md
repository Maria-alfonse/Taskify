## Project Overview
Taskify is a Django-based web application designed to streamline task management between administrators and teachers. It allows admins to assign tasks with varying priorities and enables teachers to track and complete their assigned tasks efficiently.

## Usage
- **Admins:**
  - Log in to the admin dashboard.
  - Add, edit, or delete tasks for teachers.
  - Assign priorities to tasks.
- **Teachers:**
  - Log in to view assigned tasks.
  - Mark tasks as complete once done.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Maria-alfonse/Taskify.git
    cd Taskify
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. ** Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
