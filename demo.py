import docker

import json

client = docker.APIClient(base_url='unix://var/run/docker.sock ')

# print(client.version())

# r = client.build(path='./', rm=True, tag='demo:latest')

# for i in r:
#     ss = i.strip(b'\r\n').split(b'\r\n')
#     for c in ss:
#         cc = json.loads(c)
#         if 'stream' in cc:
#             print(cc['stream'], end='')

for line in client.push('localhost:8080/teletraan/vtss:latest', stream=True):
    print(line)
    # ss = line.strip(b'\r\n').split(b'\r\n')
    # for c in ss:
    #     cc = json.loads(c)
    #     if 'stream' in cc:
    #         print(cc['stream'], end='')