from flask import Flask, render_template, request

app = Flask(__name__)

# Define the home page
@app.route('/')
def index():
    return render_template('index.html')

# Calculator logic
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                result = 'Error: Division by zero'
            else:
                result = num1 / num2
        else:
            result = 'Invalid operation'

        return render_template('index.html', result=result)

    except ValueError:
        return render_template('index.html', result='Invalid input')

if __name__ == '__main__':
    app.run(debug=True)