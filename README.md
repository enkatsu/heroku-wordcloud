# init

```bash
python -m venv venv
pip install flask gunicorn
pip freeze > requirements.txt
heroku create tweet-cloud-app
```

# local

```bash
gunicorn hello:app
```

# deploy

```bash
git push heroku master
```
