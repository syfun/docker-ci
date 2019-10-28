from flask import Flask, jsonify, request
import docker

import json


app = Flask(__name__)

client = docker.APIClient(base_url='unix://var/run/docker.sock ')


def build():
    print('build')

    for line in client.build(path='./', rm=True, tag='demo:latest'):
        ss = line.strip(b'\r\n').split(b'\r\n')
        for c in ss:
            cc = json.loads(c)
            if 'stream' in cc:
                print(cc['stream'], end='')

def push():
    print('push')
    r = client.push('localhost:8080/demo:latest')
    print(r)


@app.route('/github-webhook/', methods=['POST'])
def webhook():
    build()
    push()
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
