from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "This is the beacon set from VSCode to GitHub via Pipeline. Check the /hello endpoint too"

@application.route("/hello")
def hello():
    return "Hello World! - Now check /bye"

@application.route("/bye")
def bye():
    return "Easy to add endpoint routes"

if __name__ == "__main__":
    application.run(port=5000, debug=True)