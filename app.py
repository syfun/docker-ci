import time

from flask import Flask
from celery import Celery
from sh import docker


app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def build(image, path):
    ts = int(time.time())
    with open(f'{ts}.log', 'a') as f:
        docker("build", "-t", image, path, _out=f)


@app.route('/github-webhook/', methods=['GET'])
def webhook():
    build.delay("demo:latest", "./")
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
