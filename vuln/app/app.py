from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('app/db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        username = request.form['username']
        conn = get_db_connection()
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print("[DEBUG] Executing:", query)
        users = conn.execute(query).fetchall()
        conn.close()
        return render_template('search.html', users=users, username=username)
    return render_template('search.html', users=None)

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        return f"<h2>Thank you, {name}!</h2><p>Your comment: {comment}</p>"
    return '''
        <form method="POST">
            Name: <input name="name"><br>
            Comment: <input name="comment"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
