from flask import Blueprint, render_template, request, session, redirect, url_for, flash

page = Blueprint('page', __name__)

hardcoded_db = {
    "ticket_number": ["FLT123", "KLM334", "OR765", "TEST233"],
    "password": ["welkom123!", "test123", "ortestflight", "Wownice"]
}
    

# home page
@page.route('/')
def home():
    index = 0
    if "ticket_number" in session:
        for item in hardcoded_db["ticket_number"]:
            if session["ticket_number"] == item and session["password"] == hardcoded_db["password"][index]:
                session["login"] = "Yes"
                return render_template("home.html")
            index += 1
    return redirect(url_for("page.login"))

# login page 
@page.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    session["login"] = "No"
    if request.method == 'POST':
        ticket_number = request.form.get('ticket_number')
        password = request.form.get('password')
        username = request.form.get('username')
        session["ticket_number"] = ticket_number
        session["password"] = password
        session["username"] = username
        return redirect(url_for('page.home'))
    else:
        return render_template("login.html")

# media page
@page.route('/media')
def media():
    return render_template('media.html')
