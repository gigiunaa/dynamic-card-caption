import json
from flask import Flask, request

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

        # RETURN RAW JSON EXACTLY AS IS
        return app.response_class(
            response=json.dumps(data, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )

    except Exception as e:
        return app.response_class(
            response=json.dumps({"error": str(e)}, ensure_ascii=False),
            status=400,
            mimetype='application/json'
        )


@app.route("/", methods=["GET"])
def home():
    return "Caption Replacement API is running 🚀"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
