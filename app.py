from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

if __name__ == '__main__':
    app.run(debug=True)
