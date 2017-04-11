from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)

@profile.route('/profile/<username>')
def timeline(username):
    # Do some stuff
    return render_template('profile/timeline.html', slug = username)
