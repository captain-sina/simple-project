from flask import Flask, request, make_response, redirect, abort, render_template
app = Flask(__name__)

@app.route('/spidersite/user/<name>')
def first(user):
    if not user:
        abort(404)
    return render_template("user.html", name=user)

@app.route('/spidersite')
def main():
    response = make_response("<h2>this page carries a cookie</h2>")
    response.set_cookie('answer', '42')
    return redirect('http://google.com/')
