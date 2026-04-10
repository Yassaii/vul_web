from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Bonjour à tous 🐾</h1><p>Le jeune TP va se derouler ici</p>"

if __name__ == '__main__':
    app.run(debug=True)
    