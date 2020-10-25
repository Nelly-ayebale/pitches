from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment, Upvote, Downvote


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
