from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = 'genz-vibes-key'

PASS_FILE = 'password.txt'
DATA_FILE = 'data.txt'

def get_password():
    if not os.path.exists(PASS_FILE) or os.stat(PASS_FILE).st_size == 0:
        return None
    with open(PASS_FILE, 'r', encoding='utf-8') as f:
        return f.read().strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if get_password() is None:
        return redirect(url_for('set_password'))

    if request.method == 'POST':
        password = request.form['password']
        if password == get_password():
            session['authenticated'] = True
            return redirect(url_for('view_data'))
        else:
            flash('❌ Invalid password')
    return render_template('index.html')

@app.route('/set-password', methods=['GET', 'POST'])
def set_password():
    if get_password():
        return redirect(url_for('index'))

    if request.method == 'POST':
        password = request.form['password']
        with open(PASS_FILE, 'w', encoding='utf-8') as f:
            f.write(password)
        flash('✅ Password set successfully!')
        return redirect(url_for('index'))
    return render_template('set_password.html')

@app.route('/view')
def view_data():
    if not session.get('authenticated'):
        flash("⚠️ Please log in first!")
        return redirect(url_for('index'))

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            f.write("📝 Welcome to your data viewer.\nYou can edit this file manually.")

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    return render_template('view.html', text_content=content)

@app.route('/reset', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        old = request.form['old_password']
        new = request.form['new_password']
        if old == get_password():
            if old == new:
                flash("❌ New password can't be same as old one!")
            else:
                with open(PASS_FILE, 'w', encoding='utf-8') as f:
                    f.write(new)
                flash("✅ Password reset successful!")
                return redirect(url_for('index'))
        else:
            flash('❌ Incorrect old password!')
    return render_template('reset.html')

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    flash("👋 Logged out successfully!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
