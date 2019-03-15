from flask import Flask, render_template

from utils import get_data

app = Flask(__name__)


@app.route('/')
def main():
    data = get_data()

    content = {
        'title': data[0],
        'image': data[1],
        'details': data[4]
    }

    return render_template('index.html', **content)


if __name__ == '__main__':
    main()
