from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bedff0b16a571d2ef16ccbd6e08eb7fc'

posts = [
    {
        'author': 'Cory Schafer',
        'title': 'Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for  {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'tk@tk.in' and form.password.data == 'tk':
            flash(f'Logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Logged Failed', 'danger')
            # return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)     # RUN WITHOUT EXPORTING ENV VARIABLES 