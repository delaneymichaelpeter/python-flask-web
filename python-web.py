# Copyright 2016 Tharinda Ehelepola
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# https://github.com/tharinda221/simple-flask-web-application.git
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import *

import boto3
from urllib import urlopen
from socket import gethostname
from time   import time


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
	user = {'username': 'Peter'}
	return render_template("index.html", user=user)

@app.route('/hello')
def hello_world():
	user = {'username': 'Peter Delaney'}
	return render_template("hello.html", user=user)



def get_ec2_ip():
	url = "http://ifconfig.me"
	# url = "http://169.254.169.254/latest/meta-data/"

	# IP Address 
	data = urlopen(url + "public-ipv4").read().decode('utf-8')
	meta = {'public-ipv4': data}

	# Security Group
	data = urlopen(url + "security-groups").read().decode('utf-8')
	sg   = {'security-groups': data}

	# Instance Id
	data = urlopen(url + "instance-id").read().decode('utf-8')
	id   = {'instance-id': data}

	return render_template("machine.html", machine=data, sg=sg, id=id)


if __name__ == '__main__':
    # app.run(host="localhost", port=5000)
    app.run(host="0.0.0.0", port=5000)
