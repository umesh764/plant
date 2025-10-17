from flask import Flask, render_template

app = Flask(__name__)

# आपका डेटा, आप इसे किसी और फॉर्मेट में भी रख सकते हैं (JSON, CSV)
data = {
    "C9": {
        "1x20MM": [26.0, 35.2, 37.4],
        "1x16MM": [25.0, 34.2, 36.4],
        "2x12MM": [4, 4.2, 4],
        "3x10MM": [None, None, 16.7],
        "4x8MM": [0.5, 0.5, 0.5]
    },
    "C10": {
        "1x20MM": [36],
        "1x16MM": [36],
        "2x12MM": [30.4],
        "3x10MM": [28.1],
        "4x8MM": [15.4]
    },
    # आप C11, C12... C14 को इसी तरह जोड़ सकते हैं
}

@app.route("/")
def index():
    return render_template("test.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
