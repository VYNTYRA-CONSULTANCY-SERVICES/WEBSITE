from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask("Vyntyra Consultancy Services")
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Example: Handle Service Quote Form Submission
@app.route('/service-quote', methods=['POST'])
def service_quote():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    service = request.form.get('service')
    details = request.form.get('details')
    # Here you would process/store/send the data as needed
    flash('Thank you! Your request has been submitted. We\'ll contact you soon.')
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True)