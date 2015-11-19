from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Required, Email




app = Flask(__name__)

@app.route('/')
def index():
	# form = teamPlayers(csrf_enabled=False)
	# if request.method == 'POST' and form.validate():
	# 	player1 = form.player1.data
	# 	return redirect('www.google.com')
	# 	return render_template('index.html')
	 # if request.method == 'POST':
	 # 	flash('You were successfully logged in')
	return render_template('index.html')

class teamPlayers(Form):
	player1 = TextField("player1", validators=[Required()])


@app.route("/submit/", methods=("GET", "POST"))
def submit():
    # form = teamPlayers()
    # if form.validate_on_submit():
    #     flash("Success")
    #     return redirect(url_for("index"))
    return render_template("index.html")



    


if __name__ == '__main__':
    app.run(debug=True)