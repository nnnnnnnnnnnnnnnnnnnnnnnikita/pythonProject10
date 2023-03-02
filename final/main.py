import json
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/member')
def member():
    with open("templates/members.json", "rt", encoding="utf8") as f:
        member_list = json.loads(f.read())
    return render_template('membering.html', members=member_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
