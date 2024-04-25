from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sinopse')
def sinopse():
    return render_template('sinopse.html')

if __name__ == '__main__':
    app.run(debug=True)