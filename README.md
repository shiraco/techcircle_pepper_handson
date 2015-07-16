# rekognition

ReKognition sample

## Environment
* Python 2.7 or 3.4

## Install

```bash
$ git clone git@github.com:shiraco/rekognition.git
$ cd rekognition
$ source ./venv/bin/activate
(venv)$ pip install -r requirements.txt
```

## Setting API KEY

 Check your key from https://rekognition.com/index.php/user/account

```python:rekognition.py
# rekognition_key = os.environ.get("REKOGNITION_KEY")
rekognition_key = "YOUT_API_KEY_HERE"
# rekognition_secret = os.environ.get("REKOGNITION_SECRET")
rekognition_secret = "YOUT_API_SECRET_HERE"
```

Or if you use [autoenv](https://github.com/kennethreitz/autoenv),

```bash
$ cp .env.sample .env
$ vi .env  # update your api key
$ cd ..
$ cd rekognition  # apply api key as a environment variable
```

## Usage

```bash
% python rekognition.py who.jpg
{
    "url": "base64",
    "face_detection": [
        {
            "confidence": 1,
            "age": 42.13,
            "pose": {
                "yaw": -1.43,
                "roll": -3.63,
                "pitch": -4.51
            },
            "sex": 1,
            "boundingbox": {
                "tl": {
                    "y": 249.6,
                    "x": 52.27
                },
                "size": {
                    "width": 535.47,
                    "height": 535.47
                }
            },
            "quality": {
                "brn": 0.51,
                "shn": 1.8
            }
        }
    ],
    "ori_img_size": {
        "width": 640,
        "height": 960
    },
    "usage": {
        "status": "Succeed.",
        "quota": 3916,
        "api_id": "YOUR_API_ID"
    }
}
```
