from flask import Flask, render_template, request
import sys

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        try:
            return n * factorial(n - 1)
        except RecursionError:
            return 1

def sanitize_path(path):
    path = path.replace("../", "")
    try:
        return sanitize_path(path)
    except RecursionError:
        if path[0] == "/":
            path = path[1:]
        print(path)
        return path

@app.route('/')
def home():
    selected_theme = sanitize_path(request.args.get("theme", "themes/theme1.css"))
    theme_file = open(selected_theme, "r")
    theme_content = theme_file.read()
    theme_file.close()
    return render_template('index.html', css=theme_content)

@app.route('/', methods=['POST'])
def process_factorial():
    selected_theme = sanitize_path(request.args.get("theme", "themes/theme1.css"))

    theme_file = open(selected_theme, "r")
    theme_content = theme_file.read()
    theme_file.close()

    try:
        number = int(request.form['number'])
        if number < 0:
            error_message = "Invalid input: Please enter a non-negative integer."
            return render_template('index.html', error=error_message, css=theme_content)
        result = factorial(number)
        return render_template('index.html', result=result, css=theme_content)
    except ValueError:
        error_message = "Invalid input: Please enter a non-negative integer."
        return render_template('index.html', error=error_message, css=theme_content)

if __name__ == '__main__':
    sys.setrecursionlimit(100)
    app.run(host='0.0.0.0')
