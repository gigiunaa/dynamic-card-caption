import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/replace-caption", methods=["POST"])
def replace_caption():
    try:
        data = request.get_json()

        # Walk through JSON → find captions in cards
        messages = data.get("content", {}).get("messages", [])
        for msg in messages:
            if msg.get("type") == "cards":
                elements = msg.get("elements", [])
                
                for el in elements:
                    buttons = el.get("buttons", [])
                    for btn in buttons:
                        if btn.get("caption") == "დეტალურად":
                            btn["caption"] = "more details"

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/", methods=["GET"])
def home():
    return "Caption Replacement API is running 🚀"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
