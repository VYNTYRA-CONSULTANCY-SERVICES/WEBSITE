from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_certificate(cert_number):
    conn = sqlite3.connect('certificate_verification.db')
    cur = conn.cursor()
    cur.execute("SELECT name, course, issue_date, status FROM certificates WHERE certificate_number = ?", (cert_number,))
    row = cur.fetchone()
    conn.close()
    return row

@app.route('/', methods=['GET', 'POST'])
def verify():
    result = None
    if request.method == 'POST':
        cert_number = request.form['cert_number']
        cert = get_certificate(cert_number)
        result = cert
    return render_template('verify.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)