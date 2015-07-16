# coding:utf-8

from __future__ import print_function

import sys
import os
import requests
import json
import base64
from base64 import b64encode

rekognition_key = os.environ.get("REKOGNITION_KEY")
rekognition_secret = os.environ.get("REKOGNITION_SECRET")

def recognize(filename):

    url = "http://rekognition.com/func/api/"
    jobs = "face_gender_age"
    timeout = 30

    response = requests.post(
        url,
        data = {
            'api_key': rekognition_key,
            'api_secret': rekognition_secret,
            'jobs': jobs,
            'name_space': 'multify',
            'user_id': 'demo',
            'base64': b64encode(open(filename, 'rb').read()),
        },
        timeout = timeout
    )

    result = json.dumps(response.json(), indent = 4)
    return result

if __name__ == '__main__':
    print(recognize(sys.argv[1]))
