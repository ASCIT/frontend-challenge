from flask import *

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')

if (__name__ == '__main__'):
    app.run()

