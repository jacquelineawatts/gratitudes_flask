from flask import Flask, request, render_template, session, flash, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import datetime

app = Flask(__name__)

app.secret_key = "\xc5\\\xc27\xb4\xa7\xfa\xecVKu'\x90\xf3\xf2)\x9fH\xa2\xaf\x84j\xc7\x00"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Show homepage for users to either login or create a new account."""

    return render_template('index.html')


@app.route('/profile/<username>')
def show_profile(username):
    """Show user profile if logged in."""

    profile_user = User.get_by_username(username)
    user_entries = Entry.find_by_user(username)
    return render_template('profile.html', user=profile_user, entries=user_entries)


@app.route('/entries')
def show_entries():
    """Show recent entries, both users and those the user is following."""

    return


@app.route("/sign_up", methods=["GET"])
def sign_up():

    return render_template("sign_up.html")


@app.route("/add_user", methods=["POST"])
def add_user():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password_confirmed = request.form.get('password_confirmed')
    location = request.form.get('location')
    profile_image = request.form.get('profile_image')

    errors = User.handle_signup_form_errors(first_name, last_name, username, email, password, password_confirmed, location, profile_image)

    if errors:
        error_message = " ".join(errors)
        flash(error_message)
        return redirect('/sign_up')

    # Can't tell is this here to instantiate new user?
    else:
        User.users[username] = User.User(first_name, last_name, username, email, password, location, profile_image)
        relative_url = "/profile/" + username
        return redirect(relative_url)


# @app.route("/login", methods=["GET"])
# def show_login():
#     """Show login form."""

#     return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    username = request.form.get('username')
    user = User.get_by_username(username)

    if user:
        if request.form.get('password') == user.password:
            session['logged_in_customer_email'] = user.email
            flash("You've successfully logged in!")
            return redirect(url_for('show_profile', username=user.username))

        elif request.form.get('password') != user.password:
            flash("You entered your password incorrectly. Please try again.")
            return redirect('/')
    else:
        flash("There is no account associated with that username. Please sign up!")
        return redirect('/')


@app.route("/logout")
def logout():
    session['logged_in_customer_email'] = None
    flash("You are logged out!")
    return redirect("/")

# ----------------------------- RUN THESE FIRST --------------------------------

if __name__ == "__main__":
    app.run(debug=True)

    from model.model import connect_to_db
    from model.user import User
    from model.entry import Entry, Gratitude
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    print 'Connected to DB.'
