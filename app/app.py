from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# 로컬호스트에서 애플리케이션 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)