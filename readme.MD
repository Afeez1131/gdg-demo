In order to run this on your computer, Kindly follow the steps below.

- `git clone https://github.com/Afeez1131/gdg-demo`
- `pip install -r requirements.txt`
- `touch .env` (to create a new environmental variable in the root directory)
- Generate a new secret key, and paste in the environmental variable in the format ```SECRET_KEY=SECRET_KEY```
```
  from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
  ```
- Make migrations 
```python manage.py makemigrations```
   ```python manage.py migrate```
- Finally, run the server ```python manage.py runserver```
