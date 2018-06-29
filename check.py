from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run(port="8080")
