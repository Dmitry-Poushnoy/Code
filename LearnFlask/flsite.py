from flask import Flask, render_template
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)

menu = ["Главная", "О проекте", "Контакты"]
year = 2021

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', menu=menu, year=year)


@app.route("/about")
def about():
    cars = [1, 2, 3, 4, 5]
    return render_template('about.html', title="О проекте", menu=menu, year=year, cars=cars)


@app.route("/contact")
def contact():
    return render_template('contact.html', title="Контакты", menu=menu, year=year)


if __name__ == "__main__":
    app.run(debug=True)
