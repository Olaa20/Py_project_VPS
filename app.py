from flask import Flask, render_template
from monitor import monitor_bp  # importer ton blueprint
from blog import blog_bp

app = Flask(__name__)

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
