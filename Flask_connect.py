from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing_page.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    # Handle database insertion here
    return 'Data added to the database!'

if __name__ == '__main__':
    app.run(debug=True)