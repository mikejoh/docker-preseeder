#!/usr/bin/env python
from flask import Flask, send_file, render_template
import hashlib

app = Flask(__name__)

def get_preseed_checksum():
    return hashlib.md5(open('./preseed.cfg', 'rb').read()).hexdigest()

@app.route('/')
def index():
    md5_hash = get_preseed_checksum()
    return render_template('index.html', content=md5_hash)

@app.route('/preseed.cfg')
def preseed():
    return send_file('./preseed.cfg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
