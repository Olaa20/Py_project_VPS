from flask import Flask, render_template
from monitor import monitor_bp  # importer ton blueprint
from blog import blog_bp
from models import db

app = Flask(__name__)

# Config de la base (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key ="J3un3@dmin"

# Initialisation
db.init_app(app)

# enregistrer le module monitor
app.register_blueprint(monitor_bp, url_prefix="/monitor")
app.register_blueprint(blog_bp)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
