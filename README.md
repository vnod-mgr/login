# Django Login System

## Setup

```bash
# 1. create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. install dependencies
python3 -m pip install -r requirements.txt

# 3. run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# 4. create superuser (optional)
python3 manage.py createsuperuser

# 5. run server
python3 manage.py runserver
```

## URLs
- `/`           - home (login required)
- `/register/`  - register
- `/login/`     - login
- `/logout/`    - logout
- `/checkform/` - contact form
- `/admin/`     - admin panel

## Apps
- `account` - register, login, logout, contact form
- `default` - home page, displays messages

## Cross App
- `account/views.py` saves to `default/models.py check_form`
- `account/forms.py` has UserForm, LoginForm, CheckForm
