from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/spidersite/user/<name>')
def first(name):
    if not name:
        abort(404)
    user_agent = request.headers.get("User_agent")
    return f"<h2>{name}' profile</h2>\n<h6>browser{user_agent}"

@app.route('/spidersite')
def main():
    response = make_response("<h2>this page carries a cookie</h2>")
    response.set_cookie('answer', '42')
    return redirect('http://google.com/')
