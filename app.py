from flask import Flask, render_template
from routes import routes

app = Flask(__name__)

app.register_blueprint(routes, url_prefix="/")

@app.errorhandler(404)
def invalid_route(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost", port=5000, debug=True)
