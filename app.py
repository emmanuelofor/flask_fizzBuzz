from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.get('/')
def fizzbuzz():
    numbers = range(1,101)
    return render_template('fizzbuzz.html', numbers=numbers)


if __name__ == '__main__':
    app.run()

