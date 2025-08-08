from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the input form
@app.route('/chat')
def index():
    return render_template('index.html')

# Route to handle form submission and calculation
@app.route('/chat', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age'])
    income = float(request.form['income'])
    usage = float(request.form['usage'])  # % of credit used
    repayment = float(request.form['repayment'])  # % of on-time repayments

    # Simple example logic for alternative credit score
    # (You can replace this with your own logic or ML model)
    score = (income / 1000) + (100 - usage) + (repayment) - (age / 10)
    score = round(min(score, 850), 2)  # Cap the score at 850

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

