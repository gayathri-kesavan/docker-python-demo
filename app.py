from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    with open("resources/message.txt", "r") as file:
        message = file.read()

    return f"""
    <h1>Docker + Git + GitHub</h1>
    <p>{message}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)