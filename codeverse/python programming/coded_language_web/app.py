from flask import Flask, render_template, request
from encode_logic import encode
from decode_logic import decode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.form["text"]
        action = request.form["action"]

        if action == "encode":
            result = encode(input_text)
        elif action == "decode":
            result = decode(input_text)

    return render_template("index.html", result=result, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
