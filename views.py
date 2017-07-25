from app import app, bcrypt, db
from flask import Flask, request, redirect, render_template, session, flash, url_for, make_response

from models import Post, User
from forms import LoginForm, RegisterForm, NewPostForm

from flask_login import login_user, login_required, logout_user, LoginManager, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = u""


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


@app.route('/')
def index():
    return redirect(url_for('display_blog'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=request.form['username']).first()
        if user is not None and bcrypt.check_password_hash(
            user.password, request.form['password']
        ):
            login_user(user)
            flash('Howdy, {}!'.format(user.name.capitalize(), 'success'))
            return redirect('/blog?username={}'.format(user.name))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect('/newpost?userid={}'.format(user.id))

    return render_template('register.html', form=form, error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have loged out.')
    return redirect(url_for('display_blog'))


@app.route('/blog')
@app.route('/blog/page/<int:page>')
def display_blog(page=1):
    per_page = 3
    id = request.args.get('id')
    username = request.args.get('username')
    writers = User.query.all()
    if id:
        post = Post.query.filter_by(id=id).first()
        return render_template('post.html', post=post, writers=writers)
    elif username:
        user = User.query.filter_by(name=username).first()
        posts = Post.query.order_by(Post.pub_date.desc()).filter_by(author_id=user.id).paginate(page, per_page, False)
        return render_template('posts_user.html', posts=posts, author=user.name, writers=writers)
    else:
        posts = Post.query.order_by(Post.pub_date.desc()).paginate(page, per_page, False)
        return render_template('posts_all.html', posts=posts, writers=writers)


@app.route("/newpost", methods=['GET', 'POST'])
@login_required
def newpost():
    error = None
    form = NewPostForm()
    if form.validate_on_submit():
        newpost = Post(
            title= form.title.data,
            body = form.body.data,
            pub_date = form.pub_date.data,
            author_id = form.author_id.data
        )
        db.session.add(newpost)
        db.session.commit()
        return redirect('/blog?id='+str(newpost.id))
    else:
        return render_template("new_post.html", form=form, error=error)

