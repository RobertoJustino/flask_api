import os
from flask import Flask, render_template, jsonify, url_for, json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('layout.html')

with open('./books.json', 'r') as myfile:
    data = myfile.read()

@app.route("/booksJSON")
def booksJSON():
    return render_template('books.html', data=jsonify(data))
          
@app.route('/api/books')
def books():
    return jsonify(book)

@app.route("/api/book/<int:id>", methods=["GET"])
def get_book(id):
    book = None
    #boucle et recupere le isbn==id
    for i in book:
        for j, value in i:
            if value == id:
                book == i
    return jsonify(book)
        

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