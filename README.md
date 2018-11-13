# Google-Login


## Installation
1. Clone or download the repository. 
2. Create a new virtual environment for the project.
    ```bash
    virtualenv venv
    source venv/bin/activate
    ```
3. Install required python packages given in the requirements.txt file.
    ```bash
    pip install -r requirements.txt
    ```
4. Run Django migrations.
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Start the application.
    ```bash
    python manage.py runserver
    ```
### Note: Don't forget to add the Client and Secret Keys in settings.py.
