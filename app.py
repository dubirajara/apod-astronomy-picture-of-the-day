from flask import Flask, render_template

from utils import get_data

app = Flask(__name__)


@app.route('/')
def main():
    data = get_data()
    return render_template('index.html', **data)


if __name__ == '__main__':
    main()
