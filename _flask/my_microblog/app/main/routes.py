from flask import render_template, request, flash, redirect, url_for
from app.main import main
from app.models import *
from app.main.forms import *
from flask_login import login_required
from app import db, app
import secrets
import os
from PIL import Image

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@main.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.add(current_user)
        db.session.commit()

@main.route('/')
@main.route('/index', methods=['GET','POST'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts()\
                        .order_by(Post.date_posted.desc())\
                        .paginate(page, app.config['POSTS_PER_PAGE'], False)
    if posts.has_next:
        next_url = url_for('main.index', page=posts.next_num)
    else:
        next_url = None

    if posts.has_prev:
        prev_url = url_for('main.index', page=posts.prev_num)
    else:
        prev_url = None

    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is alive!')
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, posts=posts.items, next_url=next_url, prev_url=prev_url)


@main.route('/explore', methods=['GET','POST'])
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc())\
                      .paginate(page, app.config['POSTS_PER_PAGE'], False)
    if posts.has_next:
        next_url = url_for('main.index', page=posts.next_num)
    else:
        next_url = None
    if posts.has_prev:
        prev_url = url_for('main.index', page=posts.prev_num)
    else:
        prev_url = None
    return render_template('index.html', posts=posts.items, next_url=next_url, prev_url=prev_url)

@main.route('/user/<username>', methods=['GET','POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static',
                        filename=f'profile_pics/{user.image_file}')
    return render_template('profile.html', user=user, image_file=image_file)


@main.route('/user/<username>/edit_profile', methods=['GET','POST'])
@login_required
def edit(username):
    form = EditProfileForm()
    user = User.query.filter_by(username=username).first_or_404()
    if user != current_user:
        flash('You cannot edit another accounts')
        return redirect(url_for('main.index'))
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        if form.image_file.data:
            current_user.image_file = save_picture(form.image_file.data)
        db.session.add(current_user)
        db.session.commit()
        flash('Profile updated')
        return redirect(url_for('main.profile', username=current_user.username))

    return render_template('edit.html', form=form)


@main.route('/user/<username>/posts', methods=['GET','POST'])
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(author=user).\
        order_by(Post.date_posted.desc()).\
        paginate(page, app.config['POSTS_PER_PAGE'], False)
    if posts.has_next:
        next_url = url_for('main.user_posts', username=user.username, page = posts.next_num)
    else:
        next_url = None
    if posts.has_prev:
        prev_url = url_for('main.user_posts', username=user.username, page = posts.prev_num)
    else:
        prev_url = None
    return render_template('user_posts.html', posts=posts.items, user=user, prev_url=prev_url, next_url=next_url)


@main.route('/user/<username>/follow', methods=['POST','GET'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.profile', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('main.profile', username=username))


@main.route('/user/<username>/unfollow', methods=['POST','GET'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('main.profile', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('main.profile', username=username))

@main.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash('Your message has been sent.')
        return redirect(url_for('main.profile', username=recipient))
    return render_template('send_message.html',
                           form=form, recipient=recipient)

@main.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.date_posted.desc()).paginate(
            page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.messages', page=messages.next_num) if messages.has_prev else None
    prev_url = url_for('main.messages', page=messages.prev_num) if messages.has_prev else None
    return render_template('messages.html', messages=messages.items, next_url=next_url, prev_url=prev_url)
