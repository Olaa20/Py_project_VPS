from flask import Blueprint, render_template

blog_bp = Blueprint("blog", __name__, template_folder="templates")

# Exemple d’articles
articles = [
    {
        "id": 1,
        "title": "Mon premier VPS 🚀",
        "date": "2025-09-01",
        "summary": "Installation d’un VPS sous Ubuntu 24.04 et configuration SSH.",
        "content": """
        Dans cet article, j'explique comment j'ai pris en main mon VPS :
        - Installation Ubuntu 24.04
        - Accès SSH avec clé
        - Premier `sudo apt update && upgrade`
        """
    },
    {
        "id": 2,
        "title": "Configurer un firewall UFW 🔥",
        "date": "2025-09-10",
        "summary": "Sécurisation du VPS avec UFW (ports SSH, HTTP, HTTPS).",
        "content": """
        Étapes réalisées :
        - `sudo ufw allow OpenSSH`
        - `sudo ufw allow 80,443/tcp`
        - `sudo ufw enable`
        """
    }
]

@blog_bp.route("/blog")
def blog_home():
    return render_template("blog2.html", articles=articles)

@blog_bp.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = next((a for a in articles if a["id"] == post_id), None)
    return render_template("post.html", post=post)
