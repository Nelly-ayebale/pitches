from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment, Upvote, Downvote
from .. import db, photos
from .forms import PitchForm, CommentForm, UpvoteForm, DownvoteForm, UpdateProfile
from flask_login import login_required, current_user


@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    
    project_pitch = Pitch.query.filter_by(category= 'projectpitch')
    job_pitch = Pitch.query.filter_by(category='jobpitch')
    business_pitch = Pitch.query.filter_by(category='businesspitch')
    quote_pitch = Pitch.query.filter_by(category='quotepitch')
    pitches = Pitch.query.all()
    title = 'Home || All Pitches'

    return render_template('index.html', title=title, projectpitch = project_pitch, jobpitch= job_pitch, businesspitch= business_pitch, quotepitch= quote_pitch, pitches=pitches)

@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        pitch = form.pitch.data
        user_id = current_user
        new_pitch= Pitch(title=title, category= category, pitch = pitch, user_id=current_user._get_current_object().id)
        new_pitch.save_pitches()
        print('current_user', current_user)
        


        return redirect(url_for('main.index'))
    return render_template('new_pitch.html',form=form)

@main.route('/view_comments/<id>')
@login_required
def view_comments(id):
    comment = Comment.get_comments(id)
    title = "View Comments"
    return render_template('comment.html', comment= comment, title=title)

@main.route('/comment/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def comment(pitch_id):
    form= CommentForm()
    pitch = Pitch.query.filter_by(id= pitch_id).first()
    
    if form.validate_on_submit():
        comment = form.comment.data
       
        new_comment = Comment(comment=comment, user_id = current_user.id, pitch_id = pitch_id)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('new_comment.html', form= form,pitch_id=pitch_id)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>/pitches')
def user_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_number = Pitch.count_pitches(uname)
    

    return render_template("profile/profile.html", user=user,pitches=pitches,pitches_number=pitches_number)
