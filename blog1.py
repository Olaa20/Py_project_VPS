from flask import Blueprint, render_template
from models import db, Article

blog_bp = Blueprint("blog", __name__, template_folder="templates")

@blog_bp.route("/blog")
def blog_home():
    return render_template("blog2.html", articles=Article)

@blog_bp.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = next((a for a in articles if a["id"] == post_id), None)
    return render_template("post.html", post=post)

@blog_bp.route('/blog/new', methods=['GET', 'POST'])
def blog_new():
    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        content = request.form['content']
        new_article = Article(title=title, summary=summary, content=content)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('blog.blog_list'))
    return render_template('new_article.html')
