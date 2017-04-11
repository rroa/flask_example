from flask import Flask, request, render_template
from prefix_mid import PrefixMiddleware

application = Flask(__name__, static_url_path="", static_folder="static")
application.debug = True
application.wsgi_app = PrefixMiddleware(application.wsgi_app, prefix='/raul')

@application.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404

@application.route("/")
def hello():
    return render_template('hello.html', name="Raul")

if __name__ == "__main__":
    application.run(host='0.0.0.0')
