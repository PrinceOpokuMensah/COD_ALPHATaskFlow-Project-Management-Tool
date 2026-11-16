# TaskFlow

A collaborative project manager with group projects, members, task cards, status/priority updates, due dates and task comments.

## Run on Windows with VS Code

1. Install Python 3.11 or newer and MySQL 8 if you want MySQL.
2. Open this folder in VS Code.
3. Open Terminal and run:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

4. Visit http://127.0.0.1:8000/

SQLite is enabled by default, so the project runs without MySQL setup. To use MySQL, install `mysqlclient` or `PyMySQL`, set `DB_ENGINE=mysql`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT` in your terminal environment, and configure the MySQL driver. Never publish real passwords or secret keys.

Admin: http://127.0.0.1:8000/admin/

## Notes
This is an educational starter implementation. Test permissions, validation, and deployment security before using it with real customers or sensitive data.
