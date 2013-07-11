from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('base.html', message='Wow this is so cool.')

if __name__ == '__main__':
    app.run(debug=True)
