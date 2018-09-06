

from flask import Flask, render_template, request

# mandatory
CODEMIRROR_LANGUAGES = ['python', 'html']
# optional
CODEMIRROR_THEME = '3024-day'
# CODEMIRROR_ADDONS = (
#             ('ADDON_DIR','ADDON_NAME'),


app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
