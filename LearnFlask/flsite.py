from flask import Flask
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)

menu = ["Главная", "О проекте", "Контакты"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


@app.route("/")
@app.route("/index")
def index():
    tm = env.get_template('index.html')
    return tm.render(title="Главная страница", menu=menu)


@app.route("/about")
def about():
    cars = [1, 2, 3, 4, 5]
    tm = env.get_template('about.html')
    return tm.render(title="Страница о проекте", menu=menu, cars=cars)


@app.route("/contact")
def contact():
    tm = env.get_template('contact.html')
    return tm.render(title="Контакты", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
