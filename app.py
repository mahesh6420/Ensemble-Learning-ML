from distutils.log import debug
from flask import Flask
import os
from components.pima import routes

app = Flask(__name__)

app.register_blueprint(routes.bp)

if __name__ == "__main__" :
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)
