from . import bp as social_bp
from .models import User, Post
from flask import redirect, render_template, flash, url_for
from app.forms import PostForm
from flask_login import login_required, current_user

@social_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    posts = user_match.posts
    return render_template('user.jinja', user=user_match, posts=posts)

@social_bp.route('/post', methods = ['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        body = form.body.data
        title = form.title.data
        p = Post(title=title, body=body, user_id= current_user.id)
        p.commit()
        return redirect(url_for('social.user', username = current_user.username))
    return render_template('post.jinja', post_form = form)