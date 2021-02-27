from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import PitchForm, CommentForm, BioForm
from flask_login import login_required,current_user

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm():
    if form.validate_on_submit():
        pitch = form.my_pitches.data
        category = form.my_category.data
        new_pitch = Pitch(pitch=pitch,category=category, user_id=current_user.id)

        if category == 'Product':
            return redirect(url_for('main.product_pitches'))

        elif category == 'Marketing':
            return redirect(url_for('main.Marketing_pitches'))
        
        elif category == 'Punch Lines':
            return redirect(url_for('main.punch_lines'))
        
        elif category == 'Pickup Lines':
            return redirect(url_for('main.pickup_lines'))
        
        else:
            return redirect(url_for('.index'))

    return render_template('new_pitch.html', review_form=form)

