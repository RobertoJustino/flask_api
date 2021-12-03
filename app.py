import os
from flask import Flask, render_template, jsonify, url_for, json
app = Flask(__name__)

data = json.load(open("./books.json"))

@app.route("/")
def index():
    return render_template('layout.html')


@app.route("/booksJSON")
def booksJSON():
	return render_template('books.html', data=json.dumps(data))
          
@app.route('/api/books')
def books():
    return jsonify(books)

@app.route("/api/book/<int:id>", methods=["GET"])
def get_book(id):
	book = None
	#boucle et recupere le isbn==id
	for val in data:
		if val.get("isbn") == str(id):
			book = val
			break
	return jsonify(book)
        

@app.route('/urls')
def urls():
    return "".format(url_for("books"))


books=[
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
    app.run(debug=True, host="0.0.0.0")