from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
 return "hello world!"
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/about')
def about():
    return 'The about page'

@app.route('/urls')
def urls():
    return "".format(url_for("about"))

@app.route('/, methods=["GET", "POST"]')
def index():
    response = get_a_response()
    return response
           
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()