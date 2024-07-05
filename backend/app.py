from flask import Flask
from flask_cors import CORS
from models import mysql
from routes.user_routes import bp as user_bp
from routes.komentar_routes import bp as komentar_bp
from routes.tiket_routes import bp as tiket_bp

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')
mysql.init_app(app)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(komentar_bp, url_prefix='/komentar')
app.register_blueprint(tiket_bp, url_prefix='/tiket')



if __name__ == '__main__':
    app.run(debug=True)
