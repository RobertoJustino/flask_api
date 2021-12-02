from flask import Flask, render_template, jsonify, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('layout.html')
          
@app.route('/api/books')
def books():
    return jsonify(book)

@app.route('/api/books/<int:id>')
def book(id):
    return ""
        

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


if __name__ == '__main__':
    app.run(debug=True)