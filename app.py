import os
import redis 
from time import sleep
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            sleep(0.5)

@app.route("/")
def main():
    count = get_hit_count()
    return "hello world {}".format(count)

@app.route("/new-feature") 
def new_feature():
    return "adding new feature a new feature!"

app.run(host="0.0.0.0", port=1080, debug=True)
