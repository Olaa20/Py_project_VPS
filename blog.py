from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Article

blog_bp = Blueprint('blog', __name__)

# Liste publique des articles
@blog_bp.route('/blog')
def blog_list():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('blog2.html', articles=articles)

# Voir un article
@blog_bp.route('/blog/<int:id>')
def blog_post(id):
    article = Article.query.get_or_404(id)
    return render_template('post.html', article=article)

# 🔵 Interface admin
@blog_bp.route('/admin')
def admin_dashboard():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('admin.html', articles=articles)

# Ajouter un article
@blog_bp.route('/admin/new', methods=['GET', 'POST'])
def admin_new():
    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        content = request.form['content']
        new_article = Article(title=title, summary=summary, content=content)
        db.session.add(new_article)
        db.session.commit()
        flash("✅ Article ajouté avec succès !", "success")
        return redirect(url_for('blog.admin_dashboard'))
    return render_template('new_article.html')

# Modifier un article
@blog_bp.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.summary = request.form['summary']
        article.content = request.form['content']
        db.session.commit()
        flash("✏️ Article modifié avec succès !", "info")
        return redirect(url_for('blog.admin_dashboard'))
    return render_template('edit_article.html', article=article)

# 🔴 Supprimer un article
@blog_bp.route('/admin/delete/<int:id>')
def admin_delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash("🗑️ Article supprimé avec succès !", "danger")
    return redirect(url_for('blog.admin_dashboard'))
