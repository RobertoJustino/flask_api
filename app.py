from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
           
    
@app.route('/about')
def about():
    return 'The about page'

@app.route('/urls')
def urls():
    return "".format(url_for("about"))

@app.route('/api/books')
def about():
    return book

@app.route('/urls')
def urls():
    return "".format(url_for("books"))

book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
