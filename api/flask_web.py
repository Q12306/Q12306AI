# -*- coding: utf-8 -*-
from flask import request, Flask
import os
import server_main
app = Flask(__name__)


@app.route("/crack_captcha", methods=['POST', 'GET'])
def crack_captcha():
    res = request.json
    fetch_rep = server_main.crack_captcha(res)
    return fetch_rep


if __name__ == "__main__":
    app.run("0.0.0.0", port=8011)  # 端口为8080


