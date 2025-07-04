from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'genz-vibes-key'

PASS_FILE = 'password.txt'
IMAGE_FILE = 'image.jpg'

def get_password():
    if not os.path.exists(PASS_FILE) or os.stat(PASS_FILE).st_size == 0:
        return None
    with open(PASS_FILE, 'r') as f:
        return f.read().strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if get_password() is None:
        return redirect(url_for('set_password'))

    if request.method == 'POST':
        password = request.form['password']
        if password == get_password():
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
        with open(PASS_FILE, 'w') as f:
            f.write(password)
        flash('✅ Password set successfully!')
        return redirect(url_for('index'))
    return render_template('set_password.html')

@app.route('/view')
def view_data():
    if not os.path.exists(IMAGE_FILE):
        flash("⚠️ Image not found")
        return redirect(url_for('index'))
    return render_template('view.html', image_url=url_for('get_image'))

@app.route('/image')
def get_image():
    return send_from_directory('.', IMAGE_FILE)

@app.route('/reset', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        old = request.form['old_password']
        new = request.form['new_password']
        if old == get_password():
            if old == new:
                flash("❌ New password can't be same as old one!")
            else:
                with open(PASS_FILE, 'w') as f:
                    f.write(new)
                flash("✅ Password reset successful!")
                return redirect(url_for('index'))
        else:
            flash('❌ Incorrect old password!')
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=True)
