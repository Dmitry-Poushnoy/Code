from flask import Flask, render_template
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)

menu = ["Главная", "О проекте", "Контакты"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    cars = [1, 2, 3, 4, 5]
    return render_template('about.html', title="О проекте", menu=menu, cars=cars)


@app.route("/contact")
def contact():
    return render_template('contact.html', title="Контакты", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
