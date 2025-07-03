from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials (vulnerability!)
USERNAME = 'admin'
PASSWORD = 'password123'

@app.route('/')
def home():
    return '''
        <h2>Login</h2>
        <form action="/login" method="post">
            Username: <input type="text" name="username"/><br/>
            Password: <input type="password" name="password"/><br/>
            <input type="submit" value="Login"/>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # No input validation (vulnerability!)
    if username == USERNAME and password == PASSWORD:
        return f"<h3>Welcome, {username}!</h3>"
    else:
        return "<h3>Invalid credentials.</h3>"

if __name__ == '__main__':
    app.run(debug=True)
