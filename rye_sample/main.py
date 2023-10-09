from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

def run_app():
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
