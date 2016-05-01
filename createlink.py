#!/usr/bin/python2
import json
import os
data=json.loads('{"instance_node": "172.17.0.1", "instance_ws_paths": {}, "instance_port": 1000, "docker_id": "17abaab1a6787e792d61f2f9e5da2457aacdb36050d1105fd6bd8b9cf05a3e66", "host_name": "192.168.93.40", "instance_password": "45TVB7MC", "instance_path": "/wsvnc/172.17.0.1/1000", "instance_http_paths": {"80": "/http/172.17.0.1/3000"}, "host_port": 80, "host_ssl_port": 443, "status": 1}')
http_path=data['instance_http_paths']['80']
# mkdir -p /webdav/http/172.17.0.1/
# ln -s /home/user/ /webdav/http/172.17.0.1/3000
http_path_split = http_path.split('/')

try:
    os.stat("/webdav/")
except Exception as e:
    os.mkdir("/webdav/")
    pass

try:
    os.stat("/webdav/{}".format(http_path_split[1]))
except Exception as e:
    os.mkdir("/webdav/{}".format(http_path_split[1]))
    pass

try:
    os.stat("/webdav/{}/{}".format(http_path_split[1],http_path_split[2]))
except Exception as e:
    os.mkdir("/webdav/{}/{}".format(http_path_split[1],http_path_split[2]))
    pass

try:
    os.readlink("/webdav/{}/{}/{}".format(http_path_split[1],http_path_split[2],http_path_split[3]))
except Exception as e:
    os.symlink("/home/user/", "/webdav/{}/{}/{}".format(http_path_split[1],http_path_split[2],http_path_split[3]))
    pass
