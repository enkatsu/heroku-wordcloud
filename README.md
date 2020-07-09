

```bash
python -m venv venv
pip install flask gunicorn
pip freeze > requirements.txt
heroku create tweet-cloud-app
git push heroku master
```
