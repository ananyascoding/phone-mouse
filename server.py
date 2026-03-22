from flask import Flask, request
from flask_cors import CORS
import pyautogui

app = Flask(__name__)
CORS(app)

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    dx = data.get("dx", 0)
    dy = data.get("dy", 0)

    pyautogui.moveRel(int(dx), int(dy))
    return "OK"

@app.route("/click", methods=["POST"])
def click():
    pyautogui.click()
    return "OK"

@app.route("/right_click", methods=["POST"])
def right_click():
    pyautogui.rightClick()
    return "OK"

@app.route("/scroll", methods=["POST"])
def scroll():
    data = request.json
    dy = data.get("dy", 0)

    pyautogui.scroll(int(-dy*1))  # natural scroll
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)