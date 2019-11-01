import time

from flask import Flask
from celery import Celery
from sh import docker


app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

PROJECT_CONFIG = {
    "seely": {
        "id": 1,
        "repo": "teletraan/seely-bk",
        "branch": "dev",
        "image": "192.168.1.5:5000/teletraan/seely",
        "tag": "latest",
        "build_args": {
            "file": "",
            "path": "./"
        }
    }
}

@celery.task
def build(image, path):
    ts = int(time.time())
    with open(f'{ts}.log', 'a') as f:
        docker("build", "-t", image, path, _out=f)


@app.route('/github-webhook/<project>/', methods=['GET'])
def webhook(project):
    if project not in PROJECT_CONFIG:
        return 'no this project config'

    build.delay("demo:latest", "./")
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
