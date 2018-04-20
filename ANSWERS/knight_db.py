#!/usr/bin/env python
# (c)2015 John Strickler
import sys
import os
import sqlite3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = "I'd like to buy a wolverine"
Bootstrap(app)

DB_NAME = 'KNIGHTS.db'

class KnightForm(Form):
    name = StringField(
        "Good Sir Knight, what is your name?",
        validators=[
            DataRequired(message="Knight's named must be specified"),
            Regexp(
                r'[A-Z][a-z]{2}[a-z ]+',
                0,
                'Name must start with a capital letter and be at least 3 letters long'
            ),
        ]
    )
    quest = StringField(
        "And what is your quest?",
        validators=[DataRequired()],
        default='the Grail'
    )
    color = StringField(
        "What....is your favorite color?",
        validators=[DataRequired()]
    )
    comment = StringField(
        "You may leave a comment:",
    )
    submit = SubmitField('Off you go!')

def create_db():
    os.unlink(DB_NAME)


def update_db(form):
    print("Name:", form.name.data)
    print("Quest:", form.quest.data)
    print("Color:", form.color.data)
    print("Comment:", form.comment.data)
    with sqlite3.connect(DB_NAME) as s3conn:
        pass

@app.route('/', methods=['GET', 'POST'])
def index():
    form = KnightForm()
    if form.validate_on_submit():
        update_db(form)
    return render_template(
        'knight_db_form.html',
        form=form
    )

if __name__ == '__main__':
    if 'initdb' in sys.argv:
        create_db()
    else:
        app.run(debug=True)
