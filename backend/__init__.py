from flask import Flask

app = Flask(__name__)

# Import modules here (if any)

@app.route('/')
def home():
    return 'Welcome to the Weather App!'


if __name__ == '__main__':
    app.run(debug=True)