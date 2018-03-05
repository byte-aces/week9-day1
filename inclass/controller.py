#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_homepage():
    title = "Home"
    return render_template('index.html', \
                            title=title)

@app.route('/dashboard', methods=['GET'])
def show_dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
