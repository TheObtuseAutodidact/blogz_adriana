from app import app
from flask import Flask, request, redirect, render_template, session, flash, url_for, make_response

from models import Post, User
# from forms import LoginForm


@app.route('/')
def index():
    return redirect(url_for('display_blog'))

@app.route('/blog')
@app.route('/blog/<id>')
def display_blog():
    if request.args:
        id = request.args.get('id')
        post = Post.query.filter_by(id=id).first()
        return render_template('single_post.html', post=post)
    else:
        posts = Post.query.order_by(Post.pub_date.desc()).all()
        return render_template('posts.html', posts=posts)


@app.route("/newpost", methods=['GET', 'POST'])
def newpost():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        pub_date = request.form['pub_date']

        if title and body:
            newpost = Post(title, body)
            db.session.add(newpost)
            db.session.commit()
            return redirect('/blog?id='+str(newpost.id))
        else:
            flash("Title and body can not be empty.", "warning")
            return render_template("newpost.html", title=title, body=body, pub_date=pub_date)

    else:
        return render_template("newpost.html")
