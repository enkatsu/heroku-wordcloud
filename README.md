# init

```bash
python -m venv venv
pip install flask gunicorn
pip freeze > requirements.txt
heroku create tweet-cloud-app
```

# local

```bash
gunicorn main:app
```

```bash
FLASK_APP=main.py FLASK_ENV=development flask run --port 8080
```

# deploy

```bash
git push heroku master
```
