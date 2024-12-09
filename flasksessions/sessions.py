from flask import Flask, request, jsonify, session, redirect, url_for

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/index')
def index():
    if 'username' in session:
        return f'<p>Logged in as {session["username"]}</p>'
    return "<p>You are not logged in</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return "<p>goodbye :(</p>"

@app.route('/protected')
def protected():
    if not 'username' in session:
        return "<p>not in session bro</p>"
    return f'hello, {session["username"]} welcome to protected land'
