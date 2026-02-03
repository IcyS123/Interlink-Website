from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        try:
            # Get form data
            distance = float(request.form['distance'])
            efficiency = float(request.form['efficiency'])
            capacity = float(request.form['capacity'])

            # Calculate required diesel
            required_diesel = (distance / efficiency) - capacity
            if required_diesel < 0:
                required_diesel = 0

            return render_template('result.html', required_diesel=required_diesel)
        except ValueError:
            error_message = "Please enter valid numbers."
            return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
