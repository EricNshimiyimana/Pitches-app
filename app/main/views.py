from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db,photos
from .forms import PitchForm, CommentForm, BioForm
from flask_login import login_required,current_user
from ..models import User, Pitch, Comment
from flask import jsonify
from multiprocessing import Value

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
            return redirect(url_for('main.marketing_pitches'))
        
        elif category == 'Punch Lines':
            return redirect(url_for('main.punch_lines'))
        
        elif category == 'Pickup Lines':
            return redirect(url_for('main.pickup_lines'))
        
        else:
            return redirect(url_for('.index'))

    return render_template('new_pitch.html', review_form=form)

@main.route('/pitches/product_pitches')
def product_pitches():
    pitch = Pitch.query.all()
    product = Pitch.query.filter_by(category='Product').all()
    return render_template('product.html',product=product)

@main.route('/pitches/marketing_pitches')
def marketing_pitches():
    pitch = Pitch.query.all()
    marketing = Pitch.query.filter_by(category='Marketing').all()
    return render_template('marketing.html',marketing=marketing)

@main.route('/pitches/punch_lines')
def punch_lines():
    pitch = Pitch.query.all()
    punchlines = Pitch.query.filter_by(category='Punchlines').all()
    return render_template('punch_lines.html',punchlines=punchlines)

@main.route('/pitches/pickup_lines')
def pickup_lines():
    pitch = Pitch.query.all()
    pickuplines = Pitch.query.filter_by(category='Pickup Lines').all()
    return render_template('pickup_lines.html',pickuplines=pickuplines)
