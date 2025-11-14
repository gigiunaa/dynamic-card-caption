import json
from flask import Flask, request

app = Flask(__name__)

def replace_caption_generic(data, new_caption):
    messages = data.get("content", {}).get("messages", [])
    for msg in messages:
        if msg.get("type") == "cards":
            elements = msg.get("elements", [])
            for el in elements:
                buttons = el.get("buttons", [])
                for btn in buttons:
                    if btn.get("caption") in ["დეტალურად", "More Details", "Details Ansehen"]:
                        btn["caption"] = new_caption
    return data


@app.route("/replace-caption", methods=["POST"])
def replace_caption_en():
    try:
        data = request.get_json()
        updated = replace_caption_generic(data, "more details")

        return app.response_class(
            response=json.dumps(updated, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps({"error": str(e)}, ensure_ascii=False),
            status=400,
            mimetype='application/json'
        )


@app.route("/replace-caption-de", methods=["POST"])
def replace_caption_de():
    try:
        data = request.get_json()
        updated = replace_caption_generic(data, "Details ansehen")

        return app.response_class(
            response=json.dumps(updated, ensure_ascii=False),
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
