# diary
# Simple Diary Website

A simple diary website built using HTML, CSS, Django, and PostgreSQL. Users can create, read, update, and delete diary entries. The entries are stored in a PostgreSQL database and displayed on the website in chronological order.

## Features

- Create, read, update, and delete diary entries
- Entries displayed in order
- Responsive design

## Technologies Used

- HTML
- CSS
- Django
- PostgreSQL

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Django 3.x
- PostgreSQL
- Git

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/simple-diary-website.git
    cd simple-diary-website
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database:**

    - Create a PostgreSQL database and user.
    - Update the `DATABASES` setting in `settings.py` with your database information.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Open the website in your browser:**

    ```sh
    http://127.0.0.1:8000/
    ```


