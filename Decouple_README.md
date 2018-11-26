# Setting Up Python-Decouple
1. Make sure you have installed python-decouple.
Either install it from requirements.txt or use pip installer.

2. In your settings.py.
    * Import the ``config`` object:
        ```bash
        from decouple import config
        ```
    * Retrieve the configuration parameters:
        ```bash
        SECRET_KEY = config('SECRET_KEY')
        DEBUG = config('DEBUG', cast=bool)
        SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('DB_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
        SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('DB_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
        ```
3. To store these settings, make .env (supports .ini as well) at root level of repository as:
   ```bash
   SECRET_KEY=<Your secret here>
   DEBUG=True
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = <OAUTH2 Client Key here>
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = <OAUTH2 Secret key here>
   # other parameters
   ```
4. How it works?
    * Decouple always searches for Options in this order. Hence
        ```bash
        environment variables
        .env or .init
        default argument passed to config
        ```
    * Edit .env and use your configurations. Save it and decopule will auto-retrieve them in settings.

### Now we are ready to go!
