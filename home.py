from flask import (Blueprint, flash, g, redirect, render_template, request,)

from .db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        db = get_db()
        error = None
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        
        if not first_name:
            error = 'First name is required.'
        elif not last_name:
            error = 'Last name is required.'
        elif not email:
            error = 'Email is required.'
        elif not phone:
            error = 'Phone is required.'
        elif db.execute('Insert into waitlist (first_name, last_name, email, phone) values (?, ?, ?, ?)', (first_name, last_name, email, phone)):
            db.commit()
            return redirect('/')


    else:
        return render_template('index.html')